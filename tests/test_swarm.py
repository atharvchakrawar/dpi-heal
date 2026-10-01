"""
Comprehensive Test Suite for Project DPI-Heal
Tests Canonical Schemas, Audit Ledger, Scout Telemetry, Synthesizer, AST Verifier, Z3 Invariants, and Dynamic Router.
"""

from decimal import Decimal
import time
import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from core.ledger import AuditLedger, AuditBlock
from core.schemas import CanonicalUPIPaymentRequest
from gateway.dynamic_router import AdapterRegistry
from gateway.server import app
from swarm.orchestrator import SwarmOrchestrator
from swarm.scout import ScoutAgent
from swarm.synthesizer import SynthesizerAgent
from swarm.verifier import FormalVerifierAgent


# ==========================================
# 1. Canonical Schema Tests
# ==========================================

def test_canonical_schema_valid():
    payload = {
        "txn_id": "TXN_20261001_849204",
        "payer_vpa": "rahul@okaxis",
        "payee_vpa": "merchant@icici",
        "amount": Decimal("150.00"),
        "currency": "INR",
        "timestamp": 1727740800000,
        "auth_ref": "NPCI_RRN_123456",
    }
    req = CanonicalUPIPaymentRequest.model_validate(payload)
    assert req.txn_id == "TXN_20261001_849204"
    assert req.amount == Decimal("150.00")
    assert req.currency == "INR"


def test_canonical_schema_invalid_vpa():
    payload = {
        "txn_id": "TXN_123",
        "payer_vpa": "invalid-vpa-format",  # Missing @bank
        "payee_vpa": "merchant@icici",
        "amount": Decimal("100.00"),
        "currency": "INR",
        "timestamp": 1727740800000,
        "auth_ref": "RRN_001",
    }
    with pytest.raises(ValidationError):
        CanonicalUPIPaymentRequest.model_validate(payload)


def test_canonical_schema_invalid_amount():
    # Negative amount
    with pytest.raises(ValidationError):
        CanonicalUPIPaymentRequest.model_validate({
            "txn_id": "TXN_123",
            "payer_vpa": "user@bank",
            "payee_vpa": "user@bank",
            "amount": Decimal("-50.00"),
            "currency": "INR",
            "timestamp": 1727740800000,
            "auth_ref": "RRN_001",
        })

    # More than 2 decimal places
    with pytest.raises(ValidationError):
        CanonicalUPIPaymentRequest.model_validate({
            "txn_id": "TXN_123",
            "payer_vpa": "user@bank",
            "payee_vpa": "user@bank",
            "amount": Decimal("10.555"),
            "currency": "INR",
            "timestamp": 1727740800000,
            "auth_ref": "RRN_001",
        })


# ==========================================
# 2. Cryptographic Audit Ledger Tests
# ==========================================

def test_audit_ledger_integrity_and_tampering():
    ledger = AuditLedger(difficulty=1)
    assert ledger.count() == 1  # Genesis block
    assert ledger.verify_integrity() is True

    # Commit 2 blocks
    b1 = ledger.commit("BANK_A", "ast_hash_1", "Proof 1")
    b2 = ledger.commit("BANK_B", "ast_hash_2", "Proof 2")

    assert ledger.count() == 3
    assert b1.index == 1
    assert b2.index == 2
    assert b2.prev_hash == b1.hash
    assert ledger.verify_integrity() is True

    # Tamper with block 1 payload
    chain = ledger.get_chain()
    chain[1].client_id = "TAMPERED_BANK_ID"
    # Integrity check must detect tampering
    assert ledger.verify_integrity() is False


# ==========================================
# 3. Scout Telemetry Sliding Window Tests
# ==========================================

def test_scout_sliding_window_burst():
    alerts = []
    scout = ScoutAgent(
        failure_threshold=5,
        window_seconds=2.0,
        debounce_seconds=0.1,
        alert_callback=lambda a: alerts.append(a),
    )

    client_id = "TEST_BURST_BANK"
    dummy_payload = {"broken": True}
    dummy_err = [{"msg": "Field missing"}]

    # Ingest 4 failures (below threshold)
    for _ in range(4):
        scout.record_failure(client_id, dummy_payload, dummy_err)
    assert len(alerts) == 0

    # 5th failure reaches threshold -> triggers alert
    alert = scout.record_failure(client_id, dummy_payload, dummy_err)
    assert alert is not None
    assert len(alerts) == 1
    assert alerts[0].client_id == client_id
    assert alerts[0].failure_count >= 5


# ==========================================
# 4. Synthesizer Agent Tests
# ==========================================

def test_synthesizer_deterministic_code_generation():
    synthesizer = SynthesizerAgent(api_key=None)  # Offline fallback
    from core.schemas import AnomalyContext

    context = AnomalyContext(
        client_id="BANK_TEST_DRIFT",
        canonical_schema=CanonicalUPIPaymentRequest.model_json_schema(),
        malformed_payload={
            "txn_id": "TXN_999",
            "vpa_id": "payer@bank",
            "payee_vpa": "payee@bank",
            "txn_amount": 500.00,
            "currency": "INR",
            "timestamp": 1727740800000,
            "ref_id": "RRN_TEST",
        },
        validation_errors=[],
    )

    code = synthesizer.synthesize(context)
    assert "def adapt(payload: dict) -> dict:" in code
    assert "adapted['payer_vpa']" in code
    assert "adapted['amount']" in code


# ==========================================
# 5. Formal Verifier Double-Gate Tests
# ==========================================

def test_ast_safety_rejects_malicious_imports():
    verifier = FormalVerifierAgent()
    malicious_code = """
def adapt(payload: dict) -> dict:
    import os
    os.system("echo hacked")
    return payload
"""
    result = verifier.verify(malicious_code, {"amount": 100.0})
    assert result.passed is False
    assert "Dynamic imports" in result.reason


def test_ast_safety_rejects_dunder_traversal():
    verifier = FormalVerifierAgent()
    malicious_code = """
def adapt(payload: dict) -> dict:
    cls = payload.__class__.__bases__
    return payload
"""
    result = verifier.verify(malicious_code, {"amount": 100.0})
    assert result.passed is False
    assert "Dunder attribute access" in result.reason


def test_ast_safety_rejects_infinite_loop():
    verifier = FormalVerifierAgent()
    malicious_code = """
def adapt(payload: dict) -> dict:
    while True:
        pass
    return payload
"""
    result = verifier.verify(malicious_code, {"amount": 100.0})
    assert result.passed is False
    assert "Unbounded loops" in result.reason


def test_z3_invariant_rejects_fee_skimming():
    verifier = FormalVerifierAgent()
    # Code that deducts a 2% commission from the amount
    skimming_code = """
def adapt(payload: dict) -> dict:
    adapted = {}
    adapted['txn_id'] = payload.get('txn_id', 'TXN_001')
    adapted['payer_vpa'] = payload.get('payer_vpa', 'user@bank')
    adapted['payee_vpa'] = payload.get('payee_vpa', 'merchant@bank')
    raw_amount = float(payload.get('amount', 100.0))
    adapted['amount'] = raw_amount * 0.98
    adapted['currency'] = 'INR'
    adapted['timestamp'] = 1727740800000
    adapted['auth_ref'] = 'RRN_001'
    return adapted
"""
    result = verifier.verify(skimming_code, {"amount": 100.0})
    assert result.passed is False
    assert "Z3" in result.reason or "Monetary" in result.reason


def test_formal_verifier_approves_safe_adapter():
    verifier = FormalVerifierAgent()
    safe_code = """
def adapt(payload: dict) -> dict:
    adapted = {}
    adapted['txn_id'] = payload.get('txn_id', 'TXN_12345')
    adapted['payer_vpa'] = payload.get('vpa_id', 'user@bank')
    adapted['payee_vpa'] = payload.get('payee_vpa', 'merchant@bank')
    raw_amt = payload.get('txn_amount', 10.0)
    adapted['amount'] = f"{float(raw_amt):.2f}"
    adapted['currency'] = 'INR'
    adapted['timestamp'] = 1727740800000
    adapted['auth_ref'] = payload.get('ref_id', 'RRN_123')
    return adapted
"""
    sample_payload = {
        "txn_id": "TXN_12345",
        "vpa_id": "user@bank",
        "payee_vpa": "merchant@bank",
        "txn_amount": 250.00,
        "ref_id": "RRN_123",
    }
    result = verifier.verify(safe_code, sample_payload)
    assert result.passed is True
    assert result.z3_verified is True
    assert result.proof_signature != ""


# ==========================================
# 6. Dynamic Router Hot-Swap Tests
# ==========================================

def test_dynamic_router_hot_swap():
    router = AdapterRegistry()
    client_id = "BANK_TEST_REGISTRY"

    def mock_adapter(p: dict) -> dict:
        return {"adapted": True}

    router.register_adapter(client_id, mock_adapter, proof_hash="proof_hash_123", source_code="# test")
    assert router.get_adapter(client_id) is not None

    res = router.get_adapter(client_id)({})
    assert res == {"adapted": True}

    meta = router.get_metadata(client_id)
    assert meta.invocation_count == 1

    router.revoke_adapter(client_id)
    assert router.get_adapter(client_id) is None


# ==========================================
# 7. End-to-End FastAPI Gateway Autonomous Healing
# ==========================================

def test_fastapi_gateway_auto_healing():
    client = TestClient(app)
    bank_id = "BANK_AUTONOMOUS_TEST"

    # Step 1: Normal transaction succeeds
    valid_payload = {
        "txn_id": "TXN_NORM_001",
        "payer_vpa": "user@bank",
        "payee_vpa": "merchant@bank",
        "amount": "100.00",
        "currency": "INR",
        "timestamp": 1727740800000,
        "auth_ref": "RRN_001",
    }
    r = client.post("/api/v1/upi/pay", headers={"X-Bank-ID": bank_id}, json=valid_payload)
    assert r.status_code == 200
    assert r.json()["status"] == "SUCCESS"

    # Step 2: Broken schema requests (vpa_id instead of payer_vpa, txn_amount instead of amount)
    broken_payload = {
        "txn_id": "TXN_BROKEN_001",
        "vpa_id": "user@bank",
        "payee_vpa": "merchant@bank",
        "txn_amount": 100.00,
        "currency": "INR",
        "timestamp": 1727740800000,
        "ref_id": "RRN_001",
    }

    # First 5 fail with 422
    for _ in range(5):
        rf = client.post("/api/v1/upi/pay", headers={"X-Bank-ID": bank_id}, json=broken_payload)
        assert rf.status_code == 422

    # Step 3: Swarm has healed! 6th request with the EXACT same broken schema succeeds with ADAPTED_SUCCESS!
    rh = client.post("/api/v1/upi/pay", headers={"X-Bank-ID": bank_id}, json=broken_payload)
    assert rh.status_code == 200
    data = rh.json()
    assert data["status"] == "ADAPTED_SUCCESS"
    assert data["adapter_applied"] is True
    assert data["audit_hash"] is not None
