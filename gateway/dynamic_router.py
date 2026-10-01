"""
In-Memory Thread-Safe Dynamic Hot-Swap Adapter Registry
Enables zero-downtime, dynamic routing and payload translation per upstream client_id.
"""

import threading
import time
from typing import Any, Callable, Dict, Optional
from pydantic import BaseModel, Field


class AdapterMetadata(BaseModel):
    client_id: str
    proof_hash: str
    source_code: str
    installed_at: float
    invocation_count: int = 0
    last_invoked: Optional[float] = None


class AdapterEntry:
    def __init__(
        self,
        client_id: str,
        adapter_fn: Callable[[Dict[str, Any]], Dict[str, Any]],
        proof_hash: str,
        source_code: str = "",
    ) -> None:
        self.client_id = client_id
        self.adapter_fn = adapter_fn
        self.proof_hash = proof_hash
        self.source_code = source_code
        self.installed_at = time.time()
        self.invocation_count = 0
        self.last_invoked: Optional[float] = None

    def invoke(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        self.invocation_count += 1
        self.last_invoked = time.time()
        return self.adapter_fn(payload)

    def to_metadata(self) -> AdapterMetadata:
        return AdapterMetadata(
            client_id=self.client_id,
            proof_hash=self.proof_hash,
            source_code=self.source_code,
            installed_at=self.installed_at,
            invocation_count=self.invocation_count,
            last_invoked=self.last_invoked,
        )


class AdapterRegistry:
    """
    In-memory thread-safe registry of dynamically compiled hot-swappable translation adapters.
    """

    def __init__(self) -> None:
        self._lock = threading.RLock()
        self._adapters: Dict[str, AdapterEntry] = {}

    def register_adapter(
        self,
        client_id: str,
        adapter_fn: Callable[[Dict[str, Any]], Dict[str, Any]],
        proof_hash: str,
        source_code: str = "",
    ) -> None:
        """
        Dynamically mounts or replaces an adapter for a given upstream client_id.
        """
        with self._lock:
            entry = AdapterEntry(
                client_id=client_id,
                adapter_fn=adapter_fn,
                proof_hash=proof_hash,
                source_code=source_code,
            )
            self._adapters[client_id] = entry

    def get_adapter(
        self, client_id: str
    ) -> Optional[Callable[[Dict[str, Any]], Dict[str, Any]]]:
        """
        Retrieves the active translation function for client_id, if mounted.
        """
        with self._lock:
            entry = self._adapters.get(client_id)
            if entry is not None:
                return entry.invoke
            return None

    def get_metadata(self, client_id: str) -> Optional[AdapterMetadata]:
        with self._lock:
            entry = self._adapters.get(client_id)
            if entry is not None:
                return entry.to_metadata()
            return None

    def revoke_adapter(self, client_id: str) -> bool:
        """
        Unmounts an adapter, returning traffic for that client_id to raw validation.
        """
        with self._lock:
            if client_id in self._adapters:
                del self._adapters[client_id]
                return True
            return False

    def list_active(self) -> Dict[str, Dict[str, Any]]:
        with self._lock:
            return {
                cid: entry.to_metadata().model_dump()
                for cid, entry in self._adapters.items()
            }

    def clear(self) -> None:
        with self._lock:
            self._adapters.clear()


# Global in-memory adapter registry singleton
adapter_registry = AdapterRegistry()
