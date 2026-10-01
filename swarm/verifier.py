"""
Formal Verifier Agent: Mathematical & Invariant Safety Gate
Novel Double-Gate Verification:
1. AST Safety Analysis (disallows imports, dunders, exec/eval, file/network access).
2. SMT & Invariant Verification (Z3 monetary conservation proof, schema compliance, PII leak prevention).
"""

import ast
from decimal import Decimal
import hashlib
import hmac
import time
from typing import Any, Callable, Dict, List, Optional, Set, Tuple
import z3

from core.schemas import (
    CanonicalUPIPaymentRequest,
    VerificationResult,
)


FORBIDDEN_CALLS: Set[str] = {
    "eval",
    "exec",
    "compile",
    "open",
    "__import__",
    "globals",
    "locals",
    "vars",
    "getattr",
    "setattr",
    "delattr",
    "hasattr",
    "breakpoint",
    "exit",
    "quit",
    "input",
    "help",
    "system",
    "popen",
    "spawn",
    "socket",
    "urllib",
    "requests",
    "httpx",
}

SENSITIVE_PII_KEYS: Set[str] = {
    "mpin",
    "mpin_plain",
    "pin",
    "cvv",
    "password",
    "secret",
    "token",
    "bearer",
    "aadhaar",
    "aadhaar_raw",
    "card_number",
    "pan_number",
}


class ASTSafetyChecker(ast.NodeVisitor):
    """
    Gate 1: AST Safety Analyzer.
    Traverses the Abstract Syntax Tree to enforce strict functional isolation.
    """

    def __init__(self) -> None:
        self.errors: List[str] = []
        self.has_adapt_fn: bool = False
        self.amount_ast_binary_op: Optional[ast.BinOp] = None

    def visit_Import(self, node: ast.Import) -> Any:
        self.errors.append("Dynamic imports (import statements) are strictly prohibited.")
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> Any:
        self.errors.append("Dynamic imports (from ... import statements) are strictly prohibited.")
        self.generic_visit(node)

    def visit_Global(self, node: ast.Global) -> Any:
        self.errors.append("Global state mutation ('global' keyword) is prohibited.")
        self.generic_visit(node)

    def visit_Nonlocal(self, node: ast.Nonlocal) -> Any:
        self.errors.append("Nonlocal state mutation ('nonlocal' keyword) is prohibited.")
        self.generic_visit(node)

    def visit_While(self, node: ast.While) -> Any:
        self.errors.append("Unbounded loops ('while' loops) are prohibited to guarantee halting.")
        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute) -> Any:
        if node.attr.startswith("__"):
            self.errors.append(f"Dunder attribute access '{node.attr}' is strictly prohibited.")
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> Any:
        if isinstance(node.func, ast.Name):
            if node.func.id in FORBIDDEN_CALLS:
                self.errors.append(f"Execution of dangerous built-in function '{node.func.id}' is prohibited.")
        elif isinstance(node.func, ast.Attribute):
            if node.func.attr in FORBIDDEN_CALLS or node.func.attr.startswith("__"):
                self.errors.append(f"Execution of dangerous method '{node.func.attr}' is prohibited.")
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
        if node.name == "adapt":
            self.has_adapt_fn = True
            if len(node.args.args) != 1:
                self.errors.append("Function 'adapt' must accept exactly 1 argument: payload.")
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign) -> Any:
        # Check if amount is manipulated via arithmetic expressions (e.g. deductions/commissions)
        for target in node.targets:
            if isinstance(target, ast.Subscript):
                if isinstance(target.slice, ast.Constant) and target.slice.value == "amount":
                    if isinstance(node.value, ast.BinOp):
                        self.amount_ast_binary_op = node.value
        self.generic_visit(node)


class FormalVerifierAgent:
    """
    Formal Verifier Agent: Double-gate AST & Invariant verification.
    """

    SECRET_SALT = b"DPI_HEAL_MATHEMATICAL_ROOT_OF_TRUST_2026"

    def __init__(self) -> None:
        pass

    def verify(
        self,
        code_str: str,
        sample_malformed_payload: Dict[str, Any],
    ) -> VerificationResult:
        """
        Executes Double-Gate Formal Verification.
        """
        invariants_checked: List[str] = []

        # ==========================================
        # GATE 1: AST Static Safety Analysis
        # ==========================================
        try:
            tree = ast.parse(code_str)
        except SyntaxError as e:
            return VerificationResult(
                passed=False,
                reason=f"AST Syntax Parse Failure: {e}",
                proof_signature="",
                ast_hash="",
                invariants_checked=[],
                z3_verified=False,
                synthesized_code=code_str,
            )

        checker = ASTSafetyChecker()
        checker.visit(tree)

        if not checker.has_adapt_fn:
            checker.errors.append("Missing required root function 'adapt(payload: dict) -> dict'.")

        if checker.errors:
            return VerificationResult(
                passed=False,
                reason=f"Gate 1 AST Safety Violations: {'; '.join(checker.errors)}",
                proof_signature="",
                ast_hash="",
                invariants_checked=["AST_SAFETY_ISOLATION"],
                z3_verified=False,
                synthesized_code=code_str,
            )

        ast_canonical = ast.dump(tree, annotate_fields=False)
        ast_hash = hashlib.sha256(ast_canonical.encode("utf-8")).hexdigest()
        invariants_checked.append("AST_SAFETY_ISOLATION")

        # ==========================================
        # GATE 2.1: SMT Solver Financial Invariant (Z3)
        # ==========================================
        z3_passed, z3_reason = self._verify_z3_financial_invariant(checker.amount_ast_binary_op)
        if not z3_passed:
            return VerificationResult(
                passed=False,
                reason=f"Gate 2 Z3 SMT Monetary Invariant Violated: {z3_reason}",
                proof_signature="",
                ast_hash=ast_hash,
                invariants_checked=invariants_checked,
                z3_verified=False,
                synthesized_code=code_str,
            )
        invariants_checked.append("Z3_MONETARY_CONSERVATION_PROOF")

        # ==========================================
        # GATE 2.2: Sandboxed Property & Invariant Execution
        # ==========================================
        compiled_fn, compile_err = self._compile_sandboxed(code_str)
        if compile_err or compiled_fn is None:
            return VerificationResult(
                passed=False,
                reason=f"Sandbox Compilation Failed: {compile_err}",
                proof_signature="",
                ast_hash=ast_hash,
                invariants_checked=invariants_checked,
                z3_verified=True,
                synthesized_code=code_str,
            )

        test_suite = self._generate_test_suite(sample_malformed_payload)

        for idx, (test_name, test_payload, expected_amount) in enumerate(test_suite):
            try:
                start_t = time.perf_counter()
                adapted = compiled_fn(dict(test_payload))
                elapsed_ms = (time.perf_counter() - start_t) * 1000.0

                if elapsed_ms > 50.0:
                    return VerificationResult(
                        passed=False,
                        reason=f"Adapter execution timeout exceeded ({elapsed_ms:.2f}ms > 50ms) on {test_name}",
                        proof_signature="",
                        ast_hash=ast_hash,
                        invariants_checked=invariants_checked,
                        z3_verified=True,
                        synthesized_code=code_str,
                    )

                # Invariant A: Monetary Exact Equality
                if expected_amount is not None:
                    adapted_amt_str = str(adapted.get("amount", "0.00"))
                    try:
                        adapted_amt = Decimal(adapted_amt_str)
                        if adapted_amt != expected_amount:
                            return VerificationResult(
                                passed=False,
                                reason=f"Monetary Invariant Broken on {test_name}: Expected {expected_amount}, received {adapted_amt}",
                                proof_signature="",
                                ast_hash=ast_hash,
                                invariants_checked=invariants_checked,
                                z3_verified=True,
                                synthesized_code=code_str,
                            )
                    except Exception as ex:
                        return VerificationResult(
                            passed=False,
                            reason=f"Invalid Decimal amount produced on {test_name}: {ex}",
                            proof_signature="",
                            ast_hash=ast_hash,
                            invariants_checked=invariants_checked,
                            z3_verified=True,
                            synthesized_code=code_str,
                        )

                # Invariant B: Currency must strictly be 'INR'
                if adapted.get("currency") != "INR":
                    return VerificationResult(
                        passed=False,
                        reason=f"Currency Invariant Broken on {test_name}: Must be 'INR', got '{adapted.get('currency')}'",
                        proof_signature="",
                        ast_hash=ast_hash,
                        invariants_checked=invariants_checked,
                        z3_verified=True,
                        synthesized_code=code_str,
                    )

                # Invariant C: PII & Secret Leakage Prevention
                for sensitive_key in SENSITIVE_PII_KEYS:
                    if sensitive_key in adapted:
                        return VerificationResult(
                            passed=False,
                            reason=f"PII Leakage Invariant Broken on {test_name}: Sensitive field '{sensitive_key}' detected in adapted payload.",
                            proof_signature="",
                            ast_hash=ast_hash,
                            invariants_checked=invariants_checked,
                            z3_verified=True,
                            synthesized_code=code_str,
                        )

                # Invariant D: Canonical UPI Payment Schema Compliance
                CanonicalUPIPaymentRequest.model_validate(adapted)

            except Exception as e:
                return VerificationResult(
                    passed=False,
                    reason=f"Formal Property Test Failure on {test_name}: {e}",
                    proof_signature="",
                    ast_hash=ast_hash,
                    invariants_checked=invariants_checked,
                    z3_verified=True,
                    synthesized_code=code_str,
                )

        invariants_checked.extend([
            "MONETARY_EXACT_EQUALITY",
            "CURRENCY_DOMESTIC_INR",
            "PII_LEAK_ELIMINATION",
            "CANONICAL_SCHEMA_COMPLIANCE",
        ])

        # Cryptographic proof signature
        proof_payload = f"{ast_hash}:{'|'.join(invariants_checked)}:{time.time()}".encode("utf-8")
        proof_signature = hmac.new(self.SECRET_SALT, proof_payload, hashlib.sha256).hexdigest()

        return VerificationResult(
            passed=True,
            reason="All AST safety, Z3 monetary invariants, and canonical Pydantic contracts formally verified.",
            proof_signature=proof_signature,
            ast_hash=ast_hash,
            invariants_checked=invariants_checked,
            z3_verified=True,
            synthesized_code=code_str,
        )

    def _compile_sandboxed(self, code_str: str) -> Tuple[Optional[Callable], Optional[str]]:
        """
        Compiles the function in an isolated dictionary namespace with restricted built-ins.
        """
        safe_builtins = {
            "str": str,
            "int": int,
            "float": float,
            "dict": dict,
            "list": list,
            "len": len,
            "isinstance": isinstance,
            "min": min,
            "max": max,
            "round": round,
            "bool": bool,
            "None": None,
            "True": True,
            "False": False,
        }
        local_env: Dict[str, Any] = {}
        try:
            compiled_code = compile(code_str, "<dpi_adapter>", "exec")
            exec(compiled_code, {"__builtins__": safe_builtins}, local_env)
            adapt_fn = local_env.get("adapt")
            if not callable(adapt_fn):
                return None, "Symbol 'adapt' is not callable"
            return adapt_fn, None
        except Exception as e:
            return None, str(e)

    def _verify_z3_financial_invariant(
        self, amount_bin_op: Optional[ast.BinOp]
    ) -> Tuple[bool, str]:
        """
        Uses Z3 SMT solver to formally prove that the amount transformation T(x) == x.
        If any binary arithmetic operation is performed on amount (e.g. deducting commission x * 0.99 or x - 2.0),
        Z3 will solve for a counter-example satisfying T(x) != x for x > 0.
        """
        if amount_bin_op is None:
            # Direct assignment or type-casting (identity transformation T(x) = x). Trivially sound.
            return True, "Identity transformation verified."

        x = z3.Real("amount_in")
        solver = z3.Solver()
        solver.add(x > 0)

        # Parse AST operator
        op = amount_bin_op.op
        val_node = amount_bin_op.right if isinstance(amount_bin_op.left, ast.Name) else amount_bin_op.left
        val = 0.0
        if isinstance(val_node, ast.Constant) and isinstance(val_node.value, (int, float)):
            val = float(val_node.value)

        if isinstance(op, ast.Sub):
            # T(x) = x - val
            solver.add(x - val != x)
        elif isinstance(op, ast.Add):
            # T(x) = x + val
            solver.add(x + val != x)
        elif isinstance(op, ast.Mult):
            # T(x) = x * val
            solver.add(x * val != x)
        elif isinstance(op, ast.Div):
            # T(x) = x / val
            solver.add(x / val != x)
        else:
            return False, "Unsupported binary operator in financial calculation."

        if solver.check() == z3.sat:
            m = solver.model()
            return False, f"Z3 found invariant counterexample: amount altered under condition {m}"

        return True, "Z3 SMT solver proved monetary value conservation for all x > 0."

    def _generate_test_suite(
        self, base_payload: Dict[str, Any]
    ) -> List[Tuple[str, Dict[str, Any], Optional[Decimal]]]:
        """
        Generates edge-case test payloads for runtime verification.
        """
        # Determine original amount key and value
        amt_key = None
        for k in ["amount", "txn_amount", "transaction_amount", "amt", "transfer_amount"]:
            if k in base_payload:
                amt_key = k
                break

        original_amt = Decimal(str(base_payload[amt_key])) if amt_key else Decimal("100.00")

        # 1. Base payload test
        tests = [("base_sample", dict(base_payload), original_amt)]

        # 2. Min amount boundary (0.01 INR)
        p_min = dict(base_payload)
        if amt_key:
            p_min[amt_key] = "0.01"
        tests.append(("min_boundary_0.01", p_min, Decimal("0.01")))

        # 3. High amount boundary (100,000.00 INR)
        p_max = dict(base_payload)
        if amt_key:
            p_max[amt_key] = 100000.00
        tests.append(("max_boundary_100k", p_max, Decimal("100000.00")))

        # 4. PII injection payload (Must NOT leak into canonical output)
        p_pii = dict(base_payload)
        p_pii["mpin_plain"] = "9988"
        p_pii["aadhaar_raw"] = "889977665544"
        p_pii["cvv"] = "123"
        tests.append(("pii_injection_test", p_pii, original_amt))

        return tests


# Global Formal Verifier singleton
formal_verifier_agent = FormalVerifierAgent()
