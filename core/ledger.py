"""
Cryptographic Tamper-Evident Append-Only Audit Ledger
Ensures non-repudiation and immutable mathematical proof for every hot-swapped runtime adapter.
"""

import hashlib
import json
import threading
import time
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class AuditBlock(BaseModel):
    index: int
    timestamp: float
    client_id: str
    patch_ast_hash: str
    verifier_proof_summary: str
    prev_hash: str
    nonce: int
    hash: str

    def calculate_hash(self) -> str:
        """
        Calculates SHA-256 hash across all immutable block fields.
        """
        payload = {
            "index": self.index,
            "timestamp": self.timestamp,
            "client_id": self.client_id,
            "patch_ast_hash": self.patch_ast_hash,
            "verifier_proof_summary": self.verifier_proof_summary,
            "prev_hash": self.prev_hash,
            "nonce": self.nonce,
        }
        serialized = json.dumps(payload, sort_keys=True)
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


class AuditLedger:
    """
    Append-only cryptographically chained ledger.
    Thread-safe implementation with block integrity validation.
    """

    def __init__(self, difficulty: int = 2) -> None:
        self.difficulty = difficulty
        self.target_prefix = "0" * difficulty
        self._lock = threading.Lock()
        self._chain: List[AuditBlock] = []
        self._create_genesis_block()

    def _create_genesis_block(self) -> None:
        genesis = AuditBlock(
            index=0,
            timestamp=0.0,
            client_id="SYSTEM_ROOT_NPCI",
            patch_ast_hash="0000000000000000000000000000000000000000000000000000000000000000",
            verifier_proof_summary="GENESIS_BLOCK_ROOT_OF_TRUST",
            prev_hash="0" * 64,
            nonce=0,
            hash="",
        )
        genesis.hash = genesis.calculate_hash()
        self._chain.append(genesis)

    def commit(
        self,
        client_id: str,
        patch_ast_hash: str,
        verifier_proof_summary: str,
    ) -> AuditBlock:
        """
        Mints and commits a new immutable block recording a verified hot-swap patch.
        Uses proof-of-work mining (with configurable low difficulty) to ensure non-trivial block sealing.
        """
        with self._lock:
            prev_block = self._chain[-1]
            index = len(self._chain)
            timestamp = time.time()
            nonce = 0

            # Mine block to satisfy difficulty condition
            while True:
                candidate = AuditBlock(
                    index=index,
                    timestamp=timestamp,
                    client_id=client_id,
                    patch_ast_hash=patch_ast_hash,
                    verifier_proof_summary=verifier_proof_summary,
                    prev_hash=prev_block.hash,
                    nonce=nonce,
                    hash="",
                )
                h = candidate.calculate_hash()
                if h.startswith(self.target_prefix):
                    candidate.hash = h
                    self._chain.append(candidate)
                    return candidate
                nonce += 1

    def verify_integrity(self) -> bool:
        """
        Cryptographically validates the entire blockchain from Genesis to Tip.
        Returns True iff no block or chain link has been modified.
        """
        with self._lock:
            if not self._chain:
                return False

            # Verify Genesis
            genesis = self._chain[0]
            if genesis.index != 0 or genesis.hash != genesis.calculate_hash():
                return False

            # Verify successive blocks
            for i in range(1, len(self._chain)):
                current = self._chain[i]
                prev = self._chain[i - 1]

                # 1. Verify prev_hash pointer
                if current.prev_hash != prev.hash:
                    return False

                # 2. Verify current block's hash recomputed
                if current.hash != current.calculate_hash():
                    return False

                # 3. Verify difficulty proof
                if not current.hash.startswith(self.target_prefix):
                    return False

            return True

    def get_chain(self) -> List[AuditBlock]:
        with self._lock:
            return list(self._chain)

    def get_latest_block(self) -> AuditBlock:
        with self._lock:
            return self._chain[-1]

    def count(self) -> int:
        with self._lock:
            return len(self._chain)

    def to_dict_list(self) -> List[Dict[str, Any]]:
        with self._lock:
            return [b.model_dump() for b in self._chain]


# Global ledger singleton instance
audit_ledger = AuditLedger(difficulty=2)
