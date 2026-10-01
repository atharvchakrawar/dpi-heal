"""
Synthesizer Agent: Multi-Provider LLM & Deterministic Adapter Code Generation Engine
Supports OpenAI, Google Gemini, Anthropic Claude, Groq, and Local/Ollama models with automated verifier feedback repair loops.
"""

import ast
import json
import logging
import re
from typing import Any, Dict, Optional
import httpx

from core.config import settings
from core.schemas import AnomalyContext

logger = logging.getLogger("DPIHeal.Synthesizer")


class SynthesizerAgent:
    """
    Synthesizer Agent generates pure-function Python translation adapters
    mapping broken upstream payloads to the Gateway Canonical Schema.
    """

    SYSTEM_PROMPT = """You are an expert Compiler and API Integration Engineer specializing in Digital Public Infrastructure (UPI).
Given the Canonical Schema and the Malformed Upstream Payload, output ONLY a pure Python function named `adapt(payload: dict) -> dict` that translates the malformed input to the canonical schema.

Strict Rules:
- Do not import external modules. No 'import' or 'from ... import' statements.
- Do not modify numeric amounts or currency. Output must maintain strict monetary value conservation.
- Currency must strictly be 'INR'.
- Safely transform timestamp representations into Unix epoch milliseconds (int).
- Drop all extraneous or sensitive PII fields (e.g. mpin, pin, aadhaar, cvv) not defined in the canonical schema.
- Output ONLY executable Python code inside ```python ``` tags.
- The function must have the exact signature: def adapt(payload: dict) -> dict:
"""

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
        provider: Optional[str] = None,
        base_url: Optional[str] = None,
    ) -> None:
        self.override_api_key = api_key
        self.override_model = model
        self.override_provider = provider
        self.override_base_url = base_url

    def synthesize(self, context: AnomalyContext, verifier_feedback: str = "") -> str:
        """
        Synthesizes an adapter function string.
        Prioritizes configured LLM provider; falls back to deterministic AST synthesizer.
        """
        provider, model, api_key, base_url = self._resolve_provider()

        if provider != "deterministic" and (api_key or base_url):
            try:
                logger.info(f"Synthesizing adapter via {provider.upper()} ({model}) for {context.client_id}...")
                code = self._call_llm(
                    provider=provider,
                    model=model,
                    api_key=api_key,
                    base_url=base_url,
                    context=context,
                    verifier_feedback=verifier_feedback,
                )
                self._validate_syntax(code)
                logger.info(f"Successfully synthesized and validated AST from {provider.upper()} LLM.")
                return code
            except Exception as e:
                logger.warning(
                    f"LLM synthesis via {provider} failed or unavailable ({e}). "
                    f"Falling back to deterministic rule-based synthesizer."
                )

        logger.info(f"Using deterministic rule-based synthesizer for client: {context.client_id}")
        code = self._synthesize_deterministic(context)
        self._validate_syntax(code)
        return code

    def _resolve_provider(self) -> tuple[str, str, Optional[str], Optional[str]]:
        """
        Determines the active LLM provider, target model, API key, and base URL.
        """
        provider = self.override_provider or settings.LLM_PROVIDER
        model = self.override_model or settings.LLM_MODEL
        api_key = self.override_api_key
        base_url = self.override_base_url or settings.LLM_BASE_URL

        if self.override_api_key is None and self.override_provider is None:
            if settings.OPENAI_API_KEY:
                provider = "openai"
                model = model or "gpt-4o-mini"
                api_key = settings.OPENAI_API_KEY
            elif settings.GEMINI_API_KEY:
                provider = "gemini"
                model = model or "gemini-1.5-flash"
                api_key = settings.GEMINI_API_KEY
            elif settings.GROQ_API_KEY:
                provider = "groq"
                model = model or "llama-3.3-70b-versatile"
                api_key = settings.GROQ_API_KEY
            elif settings.ANTHROPIC_API_KEY:
                provider = "anthropic"
                model = model or "claude-3-5-haiku-20241022"
                api_key = settings.ANTHROPIC_API_KEY
            elif settings.LLM_BASE_URL:
                provider = "local"
                model = model or "llama3.2"
                api_key = "local_token"
            else:
                provider = "deterministic"
        elif provider == "openai":
            api_key = settings.OPENAI_API_KEY
            model = model or "gpt-4o-mini"
        elif provider == "gemini":
            api_key = settings.GEMINI_API_KEY
            model = model or "gemini-1.5-flash"
        elif provider == "groq":
            api_key = settings.GROQ_API_KEY
            model = model or "llama-3.3-70b-versatile"
        elif provider == "anthropic":
            api_key = settings.ANTHROPIC_API_KEY
            model = model or "claude-3-5-haiku-20241022"
        elif provider in ["ollama", "local"]:
            base_url = base_url or "http://localhost:11434/v1"
            api_key = "ollama"
            model = model or "llama3.2"

        return provider, model, api_key, base_url

    def _call_llm(
        self,
        provider: str,
        model: str,
        api_key: Optional[str],
        base_url: Optional[str],
        context: AnomalyContext,
        verifier_feedback: str = "",
    ) -> str:
        """
        Executes request to specified LLM provider with feedback repair support.
        """
        user_message_parts = [
            f"Canonical Gateway Schema:\n{json.dumps(context.canonical_schema, indent=2)}\n",
            f"Malformed Upstream Payload from Bank ({context.client_id}):\n{json.dumps(context.malformed_payload, indent=2)}\n",
            f"Ingress Validation Errors Recorded:\n{json.dumps(context.validation_errors, indent=2)}\n",
        ]

        if verifier_feedback:
            user_message_parts.append(
                f"\nCRITICAL CORRECTION REQUIRED:\nYour previous code failed formal verification with the following error:\n"
                f"{verifier_feedback}\n"
                f"Ensure all AST safety rules, Z3 monetary invariants, and canonical constraints are strictly met."
            )

        user_message_parts.append("\nGenerate the pure-function adapter:")
        user_prompt = "\n".join(user_message_parts)

        # 1. Anthropic Provider
        if provider == "anthropic":
            headers = {
                "x-api-key": api_key or "",
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            }
            body = {
                "model": model,
                "max_tokens": 1024,
                "temperature": settings.LLM_TEMPERATURE,
                "system": self.SYSTEM_PROMPT,
                "messages": [{"role": "user", "content": user_prompt}],
            }
            with httpx.Client(timeout=settings.LLM_TIMEOUT) as client:
                resp = client.post("https://api.anthropic.com/v1/messages", headers=headers, json=body)
                resp.raise_for_status()
                data = resp.json()
                text = "".join(b.get("text", "") for b in data.get("content", []))
                return self._extract_code(text)

        # 2. Google Gemini (Native Generative Language REST with OpenAI fallback)
        if provider == "gemini":
            clean_model = model.replace("models/", "")
            gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/{clean_model}:generateContent?key={api_key}"
            gemini_payload = {
                "contents": [{"parts": [{"text": user_prompt}]}],
                "systemInstruction": {"parts": [{"text": self.SYSTEM_PROMPT}]},
                "generationConfig": {"temperature": settings.LLM_TEMPERATURE},
            }
            try:
                with httpx.Client(timeout=settings.LLM_TIMEOUT) as client:
                    resp = client.post(gemini_url, json=gemini_payload)
                    if resp.status_code == 200:
                        data = resp.json()
                        candidates = data.get("candidates", [])
                        if candidates:
                            parts = candidates[0].get("content", {}).get("parts", [])
                            text = "".join(p.get("text", "") for p in parts)
                            return self._extract_code(text)
            except Exception as gemini_err:
                logger.warning(f"Gemini native endpoint notice: {gemini_err}")

            # Fallback to OpenAI-compatible endpoint
            from openai import OpenAI
            client = OpenAI(
                api_key=api_key,
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
                timeout=settings.LLM_TIMEOUT,
            )
            response = client.chat.completions.create(
                model=clean_model,
                temperature=settings.LLM_TEMPERATURE,
                messages=[
                    {"role": "system", "content": self.SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
            )
            return self._extract_code(response.choices[0].message.content or "")

        # 3. Groq Provider
        if provider == "groq":
            from openai import OpenAI

            client = OpenAI(
                api_key=api_key,
                base_url="https://api.groq.com/openai/v1",
                timeout=settings.LLM_TIMEOUT,
            )
            response = client.chat.completions.create(
                model=model,
                temperature=settings.LLM_TEMPERATURE,
                messages=[
                    {"role": "system", "content": self.SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
            )
            return self._extract_code(response.choices[0].message.content or "")

        # 4. OpenAI / Ollama / Local (Standard OpenAI client)
        from openai import OpenAI

        client_kwargs = {"timeout": settings.LLM_TIMEOUT}
        if api_key:
            client_kwargs["api_key"] = api_key
        if base_url:
            client_kwargs["base_url"] = base_url

        client = OpenAI(**client_kwargs)
        response = client.chat.completions.create(
            model=model,
            temperature=settings.LLM_TEMPERATURE,
            messages=[
                {"role": "system", "content": self.SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
        )
        return self._extract_code(response.choices[0].message.content or "")

    def _synthesize_deterministic(self, context: AnomalyContext) -> str:
        """
        Deterministic, offline semantic inference engine.
        Inspects field names, types, and error vectors to construct an exact pure-function adapter.
        """
        payload = context.malformed_payload

        # Field mapping heuristics
        mapping_rules = {
            "txn_id": ["txn_id", "transaction_id", "txnid", "txnId", "ref_id", "id", "utr"],
            "payer_vpa": ["payer_vpa", "vpa_id", "payer_vpa_id", "customer_vpa", "sender_vpa", "payerVpa", "from_vpa", "acc_vpa"],
            "payee_vpa": ["payee_vpa", "merchant_vpa", "payee_vpa_id", "beneficiary_vpa", "payeeVpa", "to_vpa", "receiver_vpa"],
            "amount": ["amount", "txn_amount", "transaction_amount", "amt", "transfer_amount", "amount_inr", "amount_rs", "value"],
            "currency": ["currency", "curr", "currency_code"],
            "timestamp": ["timestamp", "time", "tx_time", "datetime", "txn_time", "epoch_ms"],
            "auth_ref": ["auth_ref", "ref_id", "reference_no", "rrn", "auth_code", "approval_ref", "bank_ref", "txn_reference"],
        }

        resolved_source_keys: Dict[str, str] = {}
        for target, candidates in mapping_rules.items():
            for cand in candidates:
                if cand in payload:
                    resolved_source_keys[target] = cand
                    break

        # Check for nested structures (e.g. payer.vpa or data.amount)
        for k, v in payload.items():
            if isinstance(v, dict):
                for sub_k in v.keys():
                    if "vpa" in sub_k.lower() and "payer" in k.lower():
                        resolved_source_keys["payer_vpa"] = f"{k}['{sub_k}']"
                    elif "vpa" in sub_k.lower() and "payee" in k.lower():
                        resolved_source_keys["payee_vpa"] = f"{k}['{sub_k}']"

        # Generate adapter Python code lines
        lines = [
            "def adapt(payload: dict) -> dict:",
            '    """Dynamically synthesized adapter for schema drift."""',
            "    adapted = {}",
        ]

        # 1. txn_id
        src_txn = resolved_source_keys.get("txn_id")
        if src_txn:
            lines.append(f"    raw_txn = str(payload.get('{src_txn}', ''))")
            lines.append("    adapted['txn_id'] = raw_txn if raw_txn.startswith('TXN_') else f'TXN_{raw_txn}'")
        else:
            lines.append("    adapted['txn_id'] = payload.get('txn_id', 'TXN_SYNTH_001')")

        # 2. payer_vpa
        src_payer = resolved_source_keys.get("payer_vpa")
        if src_payer:
            if "['" in src_payer:
                parent_k = src_payer.split("['")[0]
                child_k = src_payer.split("['")[1].rstrip("']")
                lines.append(f"    adapted['payer_vpa'] = str(payload.get('{parent_k}', {{}}).get('{child_k}', ''))")
            else:
                lines.append(f"    adapted['payer_vpa'] = str(payload.get('{src_payer}', ''))")
        else:
            lines.append("    adapted['payer_vpa'] = str(payload.get('payer_vpa', ''))")

        # 3. payee_vpa
        src_payee = resolved_source_keys.get("payee_vpa")
        if src_payee:
            if "['" in src_payee:
                parent_k = src_payee.split("['")[0]
                child_k = src_payee.split("['")[1].rstrip("']")
                lines.append(f"    adapted['payee_vpa'] = str(payload.get('{parent_k}', {{}}).get('{child_k}', ''))")
            else:
                lines.append(f"    adapted['payee_vpa'] = str(payload.get('{src_payee}', ''))")
        else:
            lines.append("    adapted['payee_vpa'] = str(payload.get('payee_vpa', ''))")

        # 4. amount - MUST PRESERVE NUMERIC VALUE WITH EXACT EQUALITY
        src_amt = resolved_source_keys.get("amount")
        if src_amt:
            lines.append(f"    raw_amount = payload.get('{src_amt}')")
            lines.append("    if raw_amount is not None:")
            lines.append("        # Format to 2 decimal places string or float preserving original value")
            lines.append("        adapted['amount'] = f'{float(raw_amount):.2f}'")
            lines.append("    else:")
            lines.append("        adapted['amount'] = '0.00'")
        else:
            lines.append("    adapted['amount'] = str(payload.get('amount', '0.00'))")

        # 5. currency - Strictly 'INR'
        lines.append("    adapted['currency'] = 'INR'")

        # 6. timestamp
        src_time = resolved_source_keys.get("timestamp")
        if src_time:
            lines.append(f"    raw_time = payload.get('{src_time}')")
            lines.append("    if isinstance(raw_time, int):")
            lines.append("        adapted['timestamp'] = raw_time if raw_time > 10000000000 else raw_time * 1000")
            lines.append("    elif isinstance(raw_time, float):")
            lines.append("        adapted['timestamp'] = int(raw_time * 1000 if raw_time < 10000000000 else raw_time)")
            lines.append("    elif isinstance(raw_time, str):")
            lines.append("        try:")
            lines.append("            # Attempt numeric conversion")
            lines.append("            val = float(raw_time)")
            lines.append("            adapted['timestamp'] = int(val * 1000 if val < 10000000000 else val)")
            lines.append("        except ValueError:")
            lines.append("            # Fallback to standard epoch ms")
            lines.append("            adapted['timestamp'] = 1727740800000")
            lines.append("    else:")
            lines.append("        adapted['timestamp'] = 1727740800000")
        else:
            lines.append("    adapted['timestamp'] = int(payload.get('timestamp', 1727740800000))")

        # 7. auth_ref
        src_auth = resolved_source_keys.get("auth_ref")
        if src_auth:
            lines.append(f"    adapted['auth_ref'] = str(payload.get('{src_auth}', 'REF_AUTO_GENERATED'))")
        else:
            lines.append("    adapted['auth_ref'] = str(payload.get('auth_ref', 'REF_AUTO_GENERATED'))")

        # Return statement
        lines.append("    return adapted")

        return "\n".join(lines)

    def _extract_code(self, raw_output: str) -> str:
        """
        Extracts raw Python code from markdown blocks or plain text.
        """
        pattern = r"```(?:python)?\s*([\s\S]*?)```"
        matches = re.findall(pattern, raw_output, re.IGNORECASE)
        if matches:
            code = matches[0].strip()
        else:
            code = raw_output.strip()

        # Isolate def adapt(...)
        if "def adapt" in code:
            idx = code.find("def adapt")
            code = code[idx:]

        return code

    def _validate_syntax(self, code_str: str) -> None:
        """
        Validates that the synthesized code is syntactically valid Python.
        """
        try:
            tree = ast.parse(code_str)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name == "adapt":
                    return
            raise ValueError("Synthesized code must define a function named 'adapt'.")
        except SyntaxError as se:
            raise ValueError(f"Synthesized code has syntax errors: {se}")


# Global Synthesizer singleton
synthesizer_agent = SynthesizerAgent()
