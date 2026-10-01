"""
Canonical UPI Payment Schemas & Multi-Agent Telemetry Data Contracts
Compatible with Pydantic v2.
"""

from decimal import Decimal
import re
from typing import Any, Dict, List, Literal, Optional
from pydantic import BaseModel, Field, field_validator, ConfigDict


VPA_REGEX = re.compile(r"^[\w\.\-]+@[\w\-]+$")
TXN_ID_REGEX = re.compile(r"^(TXN_[A-Za-z0-9_]+|[0-9a-fA-F\-]{32,36})$")


class CanonicalUPIPaymentRequest(BaseModel):
    """
    Canonical NPCI / UPI Gateway Payment Specification (v1/v2).
    Every incoming payment must strictly conform to this schema to be processed.
    """
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    txn_id: str = Field(
        ...,
        description="Globally unique transaction identifier (e.g. TXN_20261001_849204 or UUID4)",
    )
    payer_vpa: str = Field(
        ...,
        description="Payer Virtual Payment Address (e.g. rahul@okaxis)",
    )
    payee_vpa: str = Field(
        ...,
        description="Payee Virtual Payment Address (e.g. merchant@icici)",
    )
    amount: Decimal = Field(
        ...,
        description="Monetary transaction amount in INR. Must be positive with exactly 2 decimal places.",
    )
    currency: Literal["INR"] = Field(
        default="INR",
        description="Currency code. Strictly 'INR' for domestic UPI settlement.",
    )
    timestamp: int = Field(
        ...,
        description="Unix epoch timestamp in milliseconds when transaction was initiated.",
    )
    auth_ref: str = Field(
        ...,
        description="NPCI RRN / Bank Authorization Reference Number.",
    )

    @field_validator("txn_id")
    @classmethod
    def validate_txn_id(cls, v: str) -> str:
        v = v.strip()
        if not TXN_ID_REGEX.match(v):
            raise ValueError(
                f"Invalid txn_id '{v}'. Must match prefix 'TXN_' with alphanumeric characters or UUID format."
            )
        return v

    @field_validator("payer_vpa", "payee_vpa")
    @classmethod
    def validate_vpa(cls, v: str) -> str:
        v = v.strip()
        if not VPA_REGEX.match(v):
            raise ValueError(
                f"Invalid VPA format: '{v}'. Expected format like 'user@bank'."
            )
        return v

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, v: Decimal) -> Decimal:
        if v <= Decimal("0.00"):
            raise ValueError(f"Transaction amount must be strictly positive (> 0.00). Received {v}.")
        # Ensure exact 2 decimal places
        tuple_form = v.as_tuple()
        if tuple_form.exponent < -2:
            raise ValueError(
                f"Amount {v} has more than 2 decimal places. UPI mandates exactly 2 decimal places."
            )
        # Normalize to exactly 2 decimal places
        return Decimal(f"{v:.2f}")

    @field_validator("timestamp")
    @classmethod
    def validate_timestamp(cls, v: int) -> int:
        if v <= 0:
            raise ValueError(f"Timestamp must be positive epoch milliseconds. Received {v}.")
        return v

    @field_validator("auth_ref")
    @classmethod
    def validate_auth_ref(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("auth_ref cannot be empty.")
        return v


class TransactionStatusResponse(BaseModel):
    """
    Gateway response contract for transaction ingress.
    """
    status: Literal["SUCCESS", "FAILED", "ADAPTED_SUCCESS"]
    txn_id: str
    adapter_applied: bool = False
    audit_hash: Optional[str] = None
    message: Optional[str] = None
    canonical_payload: Optional[Dict[str, Any]] = None


# ==========================================
# Agent Swarm Telemetry & Context Contracts
# ==========================================

class ValidationFailureRecord(BaseModel):
    timestamp: float
    client_id: str
    raw_payload: Dict[str, Any]
    errors: List[Dict[str, Any]]


class AnomalyAlert(BaseModel):
    """
    Emitted by Scout Agent when validation failure velocity crosses threshold.
    """
    alert_id: str
    client_id: str
    failure_count: int
    window_seconds: float
    timestamp: float
    sample_payloads: List[Dict[str, Any]]
    sample_errors: List[List[Dict[str, Any]]]


class AnomalyContext(BaseModel):
    """
    Packaged schema delta and context passed to Synthesizer Agent.
    """
    client_id: str
    canonical_schema: Dict[str, Any]
    malformed_payload: Dict[str, Any]
    validation_errors: List[Dict[str, Any]]


class VerificationResult(BaseModel):
    """
    Output of Formal Verifier Gate evaluating candidate translation adapter.
    """
    passed: bool
    reason: str
    proof_signature: str
    ast_hash: str
    invariants_checked: List[str]
    z3_verified: bool = False
    synthesized_code: str
