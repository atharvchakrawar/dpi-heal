"""
Swarm Orchestrator: Multi-Agent Coordination State Machine
Coordinates Scout -> Synthesizer -> Formal Verifier -> Hot-Swap Dispatcher & Audit Ledger.
"""

import asyncio
from enum import Enum
import logging
import threading
import time
from typing import Any, Callable, Dict, List, Optional, Tuple

from core.ledger import AuditBlock, audit_ledger
from core.schemas import AnomalyAlert, AnomalyContext, VerificationResult
from gateway.dynamic_router import adapter_registry
from swarm.scout import scout_agent
from swarm.synthesizer import synthesizer_agent
from swarm.verifier import formal_verifier_agent

logger = logging.getLogger("DPIHeal.Orchestrator")


class OrchestratorState(str, Enum):
    IDLE = "IDLE"
    INGESTING = "INGESTING"
    SYNTHESIZING = "SYNTHESIZING"
    VERIFYING = "VERIFYING"
    COMMITTING = "COMMITTING"
    HOT_SWAPPED = "HOT_SWAPPED"
    FAILED = "FAILED"


class HealingReport:
    def __init__(
        self,
        client_id: str,
        success: bool,
        duration_ms: float,
        ast_hash: str,
        proof_signature: str,
        ledger_block: Optional[AuditBlock],
        verification_result: VerificationResult,
    ) -> None:
        self.client_id = client_id
        self.success = success
        self.duration_ms = duration_ms
        self.ast_hash = ast_hash
        self.proof_signature = proof_signature
        self.ledger_block = ledger_block
        self.verification_result = verification_result

    def to_dict(self) -> Dict[str, Any]:
        return {
            "client_id": self.client_id,
            "success": self.success,
            "duration_ms": self.duration_ms,
            "ast_hash": self.ast_hash,
            "proof_signature": self.proof_signature,
            "ledger_block_index": self.ledger_block.index if self.ledger_block else None,
            "ledger_block_hash": self.ledger_block.hash if self.ledger_block else None,
            "invariants_verified": self.verification_result.invariants_checked,
        }


class SwarmOrchestrator:
    """
    Multi-Agent Coordination State Machine.
    Governs autonomous detection, synthesis, mathematical verification,
    ledger committing, and dynamic zero-downtime hot-swapping.
    """

    def __init__(
        self,
        max_retries: int = 3,
        auto_wire_scout: bool = True,
    ) -> None:
        self.max_retries = max_retries
        self.current_state = OrchestratorState.IDLE
        self._lock = threading.RLock()
        self.healing_history: List[HealingReport] = []

        if auto_wire_scout:
            scout_agent.alert_callback = self.handle_alert_sync

    def handle_alert_sync(self, alert: AnomalyAlert) -> Tuple[bool, Optional[HealingReport]]:
        """
        Synchronously handles an anomaly alert through the full multi-agent lifecycle.
        """
        with self._lock:
            start_time = time.perf_counter()
            self.current_state = OrchestratorState.INGESTING
            logger.info(f"==> Swarm Orchestrator activated for client '{alert.client_id}' (Burst count: {alert.failure_count})")

            context = scout_agent.build_anomaly_context(alert)

            feedback = ""
            for attempt in range(1, self.max_retries + 1):
                self.current_state = OrchestratorState.SYNTHESIZING
                logger.info(f"--- Attempt {attempt}/{self.max_retries}: Synthesizing translation adapter...")

                # Synthesize candidate code (with verifier feedback on retries)
                code_str = synthesizer_agent.synthesize(context, verifier_feedback=feedback)

                # Formal Verification
                self.current_state = OrchestratorState.VERIFYING
                logger.info(f"--- Attempt {attempt}/{self.max_retries}: Running Double-Gate Formal Verification...")
                v_res = formal_verifier_agent.verify(code_str, context.malformed_payload)

                if v_res.passed:
                    # Commit to cryptographic ledger & Dynamic Router
                    self.current_state = OrchestratorState.COMMITTING
                    logger.info("--- Verification Passed! Minting cryptographic audit block...")

                    proof_summary = (
                        f"Invariants: [{', '.join(v_res.invariants_checked)}] | "
                        f"Z3: {v_res.z3_verified} | Sig: {v_res.proof_signature[:16]}..."
                    )
                    block = audit_ledger.commit(
                        client_id=alert.client_id,
                        patch_ast_hash=v_res.ast_hash,
                        verifier_proof_summary=proof_summary,
                    )

                    # Dynamic compilation & mounting
                    adapt_fn, _ = formal_verifier_agent._compile_sandboxed(code_str)
                    if adapt_fn:
                        adapter_registry.register_adapter(
                            client_id=alert.client_id,
                            adapter_fn=adapt_fn,
                            proof_hash=block.hash,
                            source_code=code_str,
                        )

                    self.current_state = OrchestratorState.HOT_SWAPPED
                    duration_ms = (time.perf_counter() - start_time) * 1000.0

                    logger.info(
                        f"==> HOT-PATCH DEPLOYED for '{alert.client_id}' in {duration_ms:.2f}ms. "
                        f"Ledger Block #{block.index} [Hash: {block.hash[:16]}...]"
                    )

                    report = HealingReport(
                        client_id=alert.client_id,
                        success=True,
                        duration_ms=duration_ms,
                        ast_hash=v_res.ast_hash,
                        proof_signature=v_res.proof_signature,
                        ledger_block=block,
                        verification_result=v_res,
                    )
                    self.healing_history.append(report)
                    self.current_state = OrchestratorState.IDLE
                    return True, report

                logger.warning(f"--- Attempt {attempt} failed verification: {v_res.reason}")
                feedback = v_res.reason

            self.current_state = OrchestratorState.FAILED
            duration_ms = (time.perf_counter() - start_time) * 1000.0
            logger.error(f"==> Swarm Healing FAILED for '{alert.client_id}' after {self.max_retries} attempts.")
            return False, None

    def get_status(self) -> Dict[str, Any]:
        with self._lock:
            return {
                "state": self.current_state.value,
                "total_healed_patches": len(self.healing_history),
                "history": [r.to_dict() for r in self.healing_history],
            }


# Global Swarm Orchestrator singleton
swarm_orchestrator = SwarmOrchestrator()
