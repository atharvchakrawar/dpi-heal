"""
FastAPI UPI Gateway Server with Dynamic Interceptor Middleware
Directs traffic through hot-swappable in-memory adapters and reports telemetry to Scout.
Includes 24/7 Autonomous Background Traffic & Anomaly Ingress Engine (Auto-Pilot).
"""

from collections import deque
from contextlib import asynccontextmanager
from datetime import datetime, timezone
import logging
import random
import threading
import time
from typing import Any, Deque, Dict, List, Optional, Tuple

from fastapi import FastAPI, Header, HTTPException, Query, Request, Response, status
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import ValidationError

from core.config import settings
from core.ledger import audit_ledger
from core.schemas import (
    CanonicalUPIPaymentRequest,
    TransactionStatusResponse,
)
from gateway.dynamic_router import adapter_registry
from swarm.orchestrator import swarm_orchestrator
from swarm.scout import scout_agent
from .pages import (
    PAGE_COVER,
    PAGE_SIMULATOR,
    PAGE_ARCHITECTURE,
    PAGE_VERIFIER,
    PAGE_LEDGER,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("DPIHeal.Gateway")

# In-memory traffic metrics counter
traffic_metrics: Dict[str, int] = {
    "total_requests": 0,
    "canonical_success": 0,
    "adapted_success": 0,
    "validation_failures": 0,
}

# Real-time recent traffic ring buffer (latest 60 transactions)
recent_traffic_log: Deque[Dict[str, Any]] = deque(maxlen=60)


def execute_upi_transaction(raw_payload: Dict[str, Any], client_id: str) -> Dict[str, Any]:
    """
    Executes a UPI transaction against the dynamic gateway.
    Reroutes through active hot-patch adapters if available, validates against
    CanonicalUPIPaymentRequest, records Scout telemetry, and logs to recent traffic.
    Used by both the HTTP ingress endpoint and the Autonomous Traffic Daemon.
    """
    traffic_metrics["total_requests"] += 1
    txn_id = str(raw_payload.get("txn_id") or raw_payload.get("transaction_id") or f"TXN_{int(time.time()*1000)}")
    time_str = datetime.now().strftime("%H:%M:%S")

    # Step 1: Check dynamic hot-patch adapter
    adapter_fn = adapter_registry.get_adapter(client_id)
    if adapter_fn is not None:
        try:
            adapted_payload = adapter_fn(dict(raw_payload))
            validated_req = CanonicalUPIPaymentRequest.model_validate(adapted_payload)
            meta = adapter_registry.get_metadata(client_id)
            proof_hash = meta.proof_hash if meta else "HOT_PATCHED"

            traffic_metrics["adapted_success"] += 1
            scout_agent.record_success(client_id)

            res = {
                "status": "ADAPTED_SUCCESS",
                "status_code": 200,
                "txn_id": validated_req.txn_id,
                "client_id": client_id,
                "adapter_applied": True,
                "audit_hash": proof_hash,
                "message": f"Payload seamlessly adapted via live hot-patch for {client_id}.",
                "canonical_payload": validated_req.model_dump(mode="json"),
                "time": time_str,
            }
            recent_traffic_log.append({
                "time": time_str,
                "client_id": client_id,
                "txn_id": validated_req.txn_id,
                "status": "ADAPTED_SUCCESS",
                "status_code": 200,
                "adapter_applied": True,
            })
            return res
        except Exception as e:
            logger.error(f"Mounted adapter failed during execution for {client_id}: {e}")

    # Step 2: Validate raw payload directly against Canonical Schema
    try:
        validated_req = CanonicalUPIPaymentRequest.model_validate(raw_payload)
        traffic_metrics["canonical_success"] += 1
        scout_agent.record_success(client_id)

        res = {
            "status": "SUCCESS",
            "status_code": 200,
            "txn_id": validated_req.txn_id,
            "client_id": client_id,
            "adapter_applied": False,
            "audit_hash": None,
            "message": "Canonical payload valid.",
            "canonical_payload": validated_req.model_dump(mode="json"),
            "time": time_str,
        }
        recent_traffic_log.append({
            "time": time_str,
            "client_id": client_id,
            "txn_id": validated_req.txn_id,
            "status": "SUCCESS",
            "status_code": 200,
            "adapter_applied": False,
        })
        return res
    except ValidationError as ve:
        traffic_metrics["validation_failures"] += 1
        error_details = ve.errors()
        alert = scout_agent.record_failure(client_id, raw_payload, error_details)
        burst_info = f"Alert triggered: {alert.alert_id}" if alert else "Sliding window tracking active"
        logger.warning(
            f"Validation Failure from {client_id} (Txn: {txn_id}). {burst_info}"
        )

        res = {
            "status": "FAILED",
            "status_code": 422,
            "client_id": client_id,
            "txn_id": txn_id,
            "adapter_applied": False,
            "error": "Schema Validation Error",
            "details": [
                {
                    "loc": list(err.get("loc", [])),
                    "msg": str(err.get("msg", "")),
                    "type": str(err.get("type", "")),
                }
                for err in error_details
            ],
            "burst_telemetry": {
                "alert_emitted": alert is not None,
                "alert_id": alert.alert_id if alert else None,
            },
            "time": time_str,
        }
        recent_traffic_log.append({
            "time": time_str,
            "client_id": client_id,
            "txn_id": txn_id,
            "status": "FAILED",
            "status_code": 422,
            "adapter_applied": False,
        })
        return res


class AutonomousTrafficDaemon:
    """
    24/7 Autonomous Background Traffic & Anomaly Ingress Engine.
    Continuously generates realistic UPI transaction streams across canonical banks (HDFC)
    and regional cooperative/gramin banks with drifting schemas.
    Drives continuous autonomous detection, Z3 formal verification, and zero-downtime hot-patching.
    """

    def __init__(self, interval_sec: float = 2.0) -> None:
        self.interval_sec = interval_sec
        self.is_running = True
        self._thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()
        self.total_generated = 0
        self.last_tick_time: Optional[str] = None
        self._bank_rotation = [
            "BANK_MAHARASHTRA_COOP",
            "BANK_PUNJAB_RURAL",
            "BANK_TAMILNADU_GRAMIN",
            "BANK_KERALA_COOP",
        ]
        self._rotation_index = 0
        self._regional_burst_counter = 0

    def start(self) -> None:
        if self._thread is None or not self._thread.is_alive():
            self._stop_event.clear()
            self._thread = threading.Thread(target=self._run_loop, daemon=True, name="DPI-Autopilot")
            self._thread.start()
            logger.info("Autonomous 24/7 Traffic & Anomaly Daemon started.")

    def stop(self) -> None:
        self.is_running = False

    def toggle(self) -> bool:
        self.is_running = not self.is_running
        logger.info(f"Autonomous Daemon state toggled to: {'ACTIVE' if self.is_running else 'PAUSED'}")
        return self.is_running

    def get_status(self) -> Dict[str, Any]:
        return {
            "active": self.is_running,
            "interval_sec": self.interval_sec,
            "total_generated": self.total_generated,
            "last_tick": self.last_tick_time,
        }

    def _generate_canonical(self) -> Tuple[str, Dict[str, Any]]:
        now_ts = int(time.time() * 1000)
        num = random.randint(1000, 9999)
        return "BANK_HDFC_CANONICAL", {
            "txn_id": f"TXN_HDFC_{num}",
            "payer_vpa": f"customer_{random.randint(10, 99)}@okhdfcbank",
            "payee_vpa": f"merchant_{random.randint(10, 99)}@icici",
            "amount": f"{random.randint(50, 4999)}.00",
            "currency": "INR",
            "timestamp": now_ts,
            "auth_ref": f"RRN_{random.randint(100000, 999999)}",
        }

    def _generate_regional(self, bank_id: str) -> Tuple[str, Dict[str, Any]]:
        now_ts = int(time.time() * 1000)
        num = random.randint(1000, 9999)

        if bank_id == "BANK_MAHARASHTRA_COOP":
            return bank_id, {
                "txn_id": f"TXN_MAHA_{num}",
                "vpa_id": f"kisan_{random.randint(10, 99)}@mahacoop",
                "payee_vpa": f"market_{random.randint(10, 99)}@sbi",
                "txn_amount": f"{random.randint(250, 8500)}.00",
                "currency": "INR",
                "timestamp": now_ts,
                "ref_id": f"COOP_{random.randint(100000, 999999)}",
                "mpin_plain": "9876",
            }
        elif bank_id == "BANK_PUNJAB_RURAL":
            return bank_id, {
                "txn_id": f"TXN_PGB_{num}",
                "sender_vpa": f"farmer_{random.randint(10, 99)}@punjabgramin",
                "payee_vpa": "tractor_spares@pnb",
                "transfer_amount": f"{random.randint(500, 12000)}.00",
                "currency": "INR",
                "timestamp": now_ts,
                "rrn": f"PGB_{random.randint(100000, 999999)}",
            }
        elif bank_id == "BANK_TAMILNADU_GRAMIN":
            return bank_id, {
                "txn_id": f"TXN_TNG_{num}",
                "customer_vpa": f"selvam_{random.randint(10, 99)}@tngramin",
                "payee_vpa": "fertilizer@canara",
                "amount_inr": float(random.randint(150, 4800)),
                "currency": "INR",
                "timestamp": now_ts,
                "bank_ref": f"TNB_{random.randint(100000, 999999)}",
            }
        else:  # BANK_KERALA_COOP
            return bank_id, {
                "txn_id": f"TXN_KCB_{num}",
                "acc_vpa": f"anand_{random.randint(10, 99)}@keralacoop",
                "payee_vpa": "spices_export@sbi",
                "amount_rs": float(random.randint(300, 9500)),
                "currency": "INR",
                "timestamp": now_ts,
                "txn_reference": f"KCB_{random.randint(100000, 999999)}",
            }

    def _run_loop(self) -> None:
        time.sleep(1.5)
        while not self._stop_event.is_set():
            if self.is_running:
                try:
                    if self._regional_burst_counter > 0:
                        target_bank = self._bank_rotation[self._rotation_index % len(self._bank_rotation)]
                        bank_id, payload = self._generate_regional(target_bank)
                        self._regional_burst_counter -= 1
                        if self._regional_burst_counter == 0:
                            self._rotation_index += 1
                        sleep_time = 0.9
                    else:
                        bank_id, payload = self._generate_canonical()
                        if random.random() < 0.35:
                            self._regional_burst_counter = 5
                        sleep_time = random.uniform(1.8, 2.5)

                    execute_upi_transaction(payload, bank_id)
                    self.total_generated += 1
                    self.last_tick_time = datetime.now().strftime("%H:%M:%S")
                except Exception as ex:
                    logger.error(f"Error in AutonomousTrafficDaemon tick: {ex}")
                    sleep_time = 2.0
            else:
                sleep_time = 1.0

            time.sleep(sleep_time)


traffic_daemon = AutonomousTrafficDaemon(interval_sec=2.0)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Initializing DPI-Heal Gateway & Swarm Orchestrator...")
    traffic_daemon.start()
    yield
    traffic_daemon.stop()
    logger.info("Shutting down DPI-Heal Gateway...")


app = FastAPI(
    title=settings.GATEWAY_TITLE,
    version=settings.GATEWAY_VERSION,
    description="Autonomous Self-Healing Middleware Gateway for Digital Public Infrastructure (UPI)",
    lifespan=lifespan,
)


@app.get("/", tags=["Web Pages"])
def page_cover(request: Request):
    """
    Renders the Executive Front Cover landing page, or JSON if specifically requested.
    """
    accept = request.headers.get("accept", "")
    if "application/json" in accept and "text/html" not in accept:
        return JSONResponse(content={"status": "HEALTHY", "message": "DPI-Heal Autonomous Swarm Gateway Active", "version": settings.GATEWAY_VERSION})
    return HTMLResponse(content=PAGE_COVER)


@app.post("/", tags=["System"])
def root_post():
    """
    Root POST endpoint for interactive platform testing and health verification.
    """
    return {"status": "HEALTHY", "message": "DPI-Heal Autonomous Swarm Gateway Active", "version": settings.GATEWAY_VERSION}



@app.get("/simulator", response_class=HTMLResponse, tags=["Web Pages"])
@app.get("/mission-control", response_class=HTMLResponse, tags=["Web Pages"])
def page_simulator():
    """
    Renders the dedicated interactive Mission Control and live traffic simulator.
    """
    return HTMLResponse(content=PAGE_SIMULATOR)


@app.get("/architecture", response_class=HTMLResponse, tags=["Web Pages"])
def page_architecture():
    """
    Renders the dedicated Architecture Blueprint page.
    """
    return HTMLResponse(content=PAGE_ARCHITECTURE)


@app.get("/verifier", response_class=HTMLResponse, tags=["Web Pages"])
def page_verifier():
    """
    Renders the dedicated Z3 SMT Formal Verifier and Patent Core page.
    """
    return HTMLResponse(content=PAGE_VERIFIER)


@app.get("/ledger-explorer", response_class=HTMLResponse, tags=["Web Pages"])
def page_ledger():
    """
    Renders the dedicated Cryptographic Blockchain Ledger Explorer page.
    """
    return HTMLResponse(content=PAGE_LEDGER)


@app.get("/health", tags=["System"])
def health_check() -> Dict[str, str]:
    return {"status": "HEALTHY", "version": settings.GATEWAY_VERSION}


@app.post(
    "/api/v1/upi/pay",
    response_model=TransactionStatusResponse,
    status_code=status.HTTP_200_OK,
    tags=["Ingress Payment API"],
)
async def process_payment(
    request: Request,
    x_bank_id: Optional[str] = Header(None, alias="X-Bank-ID"),
    bank_id_param: Optional[str] = Query(None, alias="bank_id"),
):
    """
    Ingress endpoint for UPI transactions.
    Dynamically routes through verified hot-swap adapter if available for the given bank ID.
    On failure without adapter, logs anomaly burst telemetry to Scout Agent.
    """
    try:
        raw_payload = await request.json()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Malformed JSON in request body",
        )

    client_id = x_bank_id or bank_id_param or raw_payload.get("bank_id") or "UNKNOWN_CLIENT"
    result = execute_upi_transaction(raw_payload, client_id)

    if result["status_code"] == 422:
        return JSONResponse(status_code=422, content=result)

    return TransactionStatusResponse(
        status=result["status"],
        txn_id=result["txn_id"],
        adapter_applied=result["adapter_applied"],
        audit_hash=result["audit_hash"],
        message=result["message"],
        canonical_payload=result["canonical_payload"],
    )


@app.get("/api/v1/autopilot", tags=["Autonomous Swarm Daemon"])
def get_autopilot_status() -> Dict[str, Any]:
    """
    Returns live state of the 24/7 autonomous background traffic & anomaly engine.
    """
    return traffic_daemon.get_status()


@app.post("/api/v1/autopilot/toggle", tags=["Autonomous Swarm Daemon"])
def toggle_autopilot() -> Dict[str, Any]:
    """
    Toggles the 24/7 background autopilot on or off.
    """
    active = traffic_daemon.toggle()
    return {"active": active, "status": traffic_daemon.get_status()}


@app.get("/api/v1/metrics", tags=["Telemetry & Observability"])
def get_metrics() -> Dict[str, Any]:
    """
    Returns live gateway telemetry, traffic counters, active adapters, ledger state,
    recent streaming traffic, and autopilot state.
    """
    scout_stats = scout_agent.get_metrics()
    active_adapters = adapter_registry.list_active()
    orchestrator_status = swarm_orchestrator.get_status()

    return {
        "traffic": dict(traffic_metrics),
        "scout_telemetry": scout_stats,
        "active_hot_patches_count": len(active_adapters),
        "active_hot_patches": active_adapters,
        "audit_ledger_blocks": audit_ledger.count(),
        "audit_ledger_integrity": audit_ledger.verify_integrity(),
        "orchestrator_state": orchestrator_status["state"],
        "healing_history": orchestrator_status["history"],
        "recent_traffic": list(recent_traffic_log),
        "autopilot": traffic_daemon.get_status(),
    }


@app.get("/api/v1/ledger", tags=["Audit & Non-Repudiation"])
def get_audit_ledger() -> Dict[str, Any]:
    """
    Returns cryptographic append-only audit trail and integrity verification.
    """
    is_valid = audit_ledger.verify_integrity()
    blocks = audit_ledger.to_dict_list()
    return {
        "integrity_verified": is_valid,
        "total_blocks": len(blocks),
        "blocks": blocks,
    }


@app.get("/api/v1/adapters", tags=["Dynamic Router"])
def list_adapters() -> Dict[str, Any]:
    """
    Lists all currently hot-swapped adapters and their invocation telemetry.
    """
    return {
        "count": len(adapter_registry.list_active()),
        "adapters": adapter_registry.list_active(),
    }


@app.delete("/api/v1/adapters/{client_id}", tags=["Dynamic Router"])
def revoke_adapter(client_id: str) -> Dict[str, Any]:
    """
    Revokes an active hot-patch, reverting traffic to raw canonical schema validation.
    Also resets Scout telemetry window and debounce timer for that client for repeatable testing.
    """
    revoked = adapter_registry.revoke_adapter(client_id)
    scout_agent.reset_client(client_id)
    return {
        "status": "REVOKED" if revoked else "RESET",
        "client_id": client_id,
        "adapter_was_active": revoked,
    }
