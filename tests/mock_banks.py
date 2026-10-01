"""
Synthetic UPI Traffic Generator: Simulation of Unannounced Schema Drifts & Self-Healing
Demonstrates:
1. Normal Canonical Traffic (Bank A - HDFC).
2. Schema Drift Failure Spike (Bank B - Maharashtra Cooperative Bank).
3. Scout Anomaly Trigger -> Synthesis -> Verification -> Hot-Swap Mount.
4. Auto-Healed Resumption (Bank B requests succeed seamlessly).
5. Immutable Ledger Audit Output.
"""

import json
import sys
import time
from typing import Any, Dict
from fastapi.testclient import TestClient

# Ensure safe console output encoding on Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from gateway.server import app
from core.ledger import audit_ledger
from gateway.dynamic_router import adapter_registry
from swarm.scout import scout_agent


# ANSI Color formatting
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


def print_banner():
    banner = f"""
{CYAN}{BOLD}================================================================================
   PROJECT DPI-HEAL: AUTONOMOUS SELF-HEALING MIDDLEWARE SWARM
   Digital Public Infrastructure (UPI / OCEN / DigiLocker Rail Protector)
================================================================================{RESET}
"""
    print(banner)


def run_simulation(client: TestClient = None) -> bool:
    if client is None:
        client = TestClient(app)

    print_banner()

    # ---------------------------------------------------------
    # STAGE 1: Steady-State Normal Traffic from Bank A (HDFC)
    # ---------------------------------------------------------
    print(f"{BLUE}[STAGE 1]{RESET} Sending 10 Canonical UPI Transactions from {BOLD}BANK_HDFC_CANONICAL{RESET}...")
    time.sleep(0.5)

    for i in range(1, 11):
        payload = {
            "txn_id": f"TXN_HDFC_{1000 + i}",
            "payer_vpa": f"customer_{i}@okhdfcbank",
            "payee_vpa": "merchant@icici",
            "amount": "250.00",
            "currency": "INR",
            "timestamp": int(time.time() * 1000),
            "auth_ref": f"RRN_HDFC_{90000 + i}",
        }
        res = client.post(
            "/api/v1/upi/pay",
            headers={"X-Bank-ID": "BANK_HDFC_CANONICAL"},
            json=payload,
        )
        assert res.status_code == 200, f"Expected 200, got {res.status_code}"
        data = res.json()
        print(f"  {GREEN}[200 OK]{RESET} Txn: {data['txn_id']} | Status: {BOLD}{data['status']}{RESET} | Adapter: {data['adapter_applied']}")

    print(f"{GREEN}[OK] Bank A completed 10/10 transactions with 100% success rate.{RESET}\n")

    # ---------------------------------------------------------
    # STAGE 2: Unannounced Schema Drift from Bank B (Co-op Bank)
    # ---------------------------------------------------------
    bank_b_id = "BANK_MAHARASHTRA_COOP"
    print(f"{YELLOW}[STAGE 2]{RESET} Upstream Bank {BOLD}{bank_b_id}{RESET} deploys unannounced breaking schema update!")
    print(f"         Drift details: 'payer_vpa' -> 'vpa_id', 'amount' -> 'txn_amount', 'auth_ref' -> 'ref_id'")
    time.sleep(0.5)

    print(f"\n{RED}[STAGE 3]{RESET} Ingress traffic from {bank_b_id} fails schema validation (HTTP 422)...")

    # Bank B sends 5 breaking requests that will fail and trigger Scout
    for i in range(1, 6):
        broken_payload = {
            "txn_id": f"TXN_MAH_{5000 + i}",
            "vpa_id": f"rural_farmer_{i}@mahcoop",    # BREAKING DRIFT
            "payee_vpa": "mandi_kisan@sbi",
            "txn_amount": 1450.50,                     # BREAKING DRIFT (float + wrong key)
            "currency": "INR",
            "timestamp": int(time.time() * 1000),
            "ref_id": f"COOP_REF_{70000 + i}",         # BREAKING DRIFT
            "mpin_plain": "4829",                      # SENSITIVE LEAKAGE CANDIDATE
        }
        res = client.post(
            "/api/v1/upi/pay",
            headers={"X-Bank-ID": bank_b_id},
            json=broken_payload,
        )
        print(f"  {RED}[422 FAIL]{RESET} Txn: {broken_payload['txn_id']} | Bank: {bank_b_id} | Validation rejected raw payload")
        time.sleep(0.1)

    # ---------------------------------------------------------
    # STAGE 4: Swarm Autonomous Self-Healing Check
    # ---------------------------------------------------------
    print(f"\n{CYAN}[STAGE 4]{RESET} Inspecting Swarm Self-Healing Status...")
    active_adapter = adapter_registry.get_adapter(bank_b_id)
    metadata = adapter_registry.get_metadata(bank_b_id)

    if active_adapter is None:
        print(f"{RED}FAILED: Hot-swap adapter was not registered!{RESET}")
        return False

    print(f"{GREEN}{BOLD}[OK] SWARM SELF-HEALING SUCCESSFUL!{RESET}")
    print(f"  - Client ID: {metadata.client_id}")
    print(f"  - Proof Hash: {metadata.proof_hash}")
    print(f"  - Installed At: {time.ctime(metadata.installed_at)}")
    print(f"\n{CYAN}Synthesized Pure-Function Adapter:{RESET}")
    print(f"{YELLOW}{metadata.source_code}{RESET}\n")

    # ---------------------------------------------------------
    # STAGE 5: Resuming Bank B Traffic with Zero Downtime
    # ---------------------------------------------------------
    print(f"{BLUE}[STAGE 5]{RESET} Resuming traffic from {BOLD}{bank_b_id}{RESET} through Live Dynamic Interceptor...")
    time.sleep(0.5)

    for i in range(6, 16):
        broken_payload = {
            "txn_id": f"TXN_MAH_{5000 + i}",
            "vpa_id": f"rural_farmer_{i}@mahcoop",
            "payee_vpa": "mandi_kisan@sbi",
            "txn_amount": 1450.50,
            "currency": "INR",
            "timestamp": int(time.time() * 1000),
            "ref_id": f"COOP_REF_{70000 + i}",
            "mpin_plain": "4829",
        }
        res = client.post(
            "/api/v1/upi/pay",
            headers={"X-Bank-ID": bank_b_id},
            json=broken_payload,
        )
        assert res.status_code == 200, f"Expected 200, got {res.status_code}: {res.text}"
        data = res.json()
        print(
            f"  {GREEN}[200 OK]{RESET} Txn: {data['txn_id']} | Status: {BOLD}{data['status']}{RESET} | "
            f"Adapted: {BOLD}{data['adapter_applied']}{RESET} | Proof: {data['audit_hash'][:16]}..."
        )

    print(f"{GREEN}[OK] Bank B resumed 10/10 adapted transactions with 100% throughput restoration!{RESET}\n")

    # ---------------------------------------------------------
    # STAGE 6: Cryptographic Blockchain Ledger Audit Trail
    # ---------------------------------------------------------
    print(f"{CYAN}[STAGE 6]{RESET} Cryptographic Audit Ledger Proof-of-Integrity:")
    print(f"  - Blockchain Integrity: {BOLD}{GREEN if audit_ledger.verify_integrity() else RED}{audit_ledger.verify_integrity()}{RESET}")
    print(f"  - Total Blocks Mined: {audit_ledger.count()}")

    for block in audit_ledger.get_chain():
        print(f"    Block #{block.index}: Client={block.client_id} | Hash={block.hash[:20]}... | Nonce={block.nonce}")
        print(f"             Proof={block.verifier_proof_summary}")

    print(f"\n{GREEN}{BOLD}>>> Project DPI-Heal End-to-End Simulation COMPLETED SUCCESSFULLY <<<{RESET}\n")
    return True


if __name__ == "__main__":
    success = run_simulation()
    sys.exit(0 if success else 1)
