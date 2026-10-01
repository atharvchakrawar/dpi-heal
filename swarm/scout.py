"""
Scout Agent: Telemetry Analyzer & Anomaly Ingress Engine
Maintains sliding-window error velocities and triggers targeted anomaly alerts for upstream schema drifts.
"""

from collections import deque
import threading
import time
import uuid
from typing import Any, Callable, Deque, Dict, List, Optional, Tuple

from core.config import settings
from core.schemas import (
    AnomalyAlert,
    AnomalyContext,
    CanonicalUPIPaymentRequest,
)


class FailureRecord:
    def __init__(self, timestamp: float, raw_payload: Dict[str, Any], errors: List[Dict[str, Any]]) -> None:
        self.timestamp = timestamp
        self.raw_payload = raw_payload
        self.errors = errors


class ScoutAgent:
    """
    Scout Agent monitors ingress API failures, calculates real-time failure velocity
    in a sliding time window, and isolates breaking upstream schema drifts.
    """

    def __init__(
        self,
        failure_threshold: int = settings.SCOUT_FAILURE_THRESHOLD,
        window_seconds: float = settings.SCOUT_WINDOW_SECONDS,
        debounce_seconds: float = settings.SCOUT_DEBOUNCE_SECONDS,
        alert_callback: Optional[Callable[[AnomalyAlert], None]] = None,
    ) -> None:
        self.failure_threshold = failure_threshold
        self.window_seconds = window_seconds
        self.debounce_seconds = debounce_seconds
        self.alert_callback = alert_callback

        self._lock = threading.RLock()
        self._windows: Dict[str, Deque[FailureRecord]] = {}
        self._last_alert_timestamps: Dict[str, float] = {}
        self._total_failures: Dict[str, int] = {}
        self._total_successes: Dict[str, int] = {}

    def record_failure(
        self,
        client_id: str,
        raw_payload: Dict[str, Any],
        errors: List[Dict[str, Any]],
    ) -> Optional[AnomalyAlert]:
        """
        Ingests a 422/400 validation failure into the sliding window for the given client_id.
        Triggers an AnomalyAlert if error burst velocity crosses threshold.
        """
        with self._lock:
            now = time.time()
            self._total_failures[client_id] = self._total_failures.get(client_id, 0) + 1

            if client_id not in self._windows:
                self._windows[client_id] = deque()

            window = self._windows[client_id]
            # Prune obsolete events outside the sliding window
            cutoff = now - self.window_seconds
            while window and window[0].timestamp < cutoff:
                window.popleft()

            # Append current failure record
            window.append(FailureRecord(now, raw_payload, errors))

            # Check if burst velocity crosses failure_threshold
            if len(window) >= self.failure_threshold:
                last_alert = self._last_alert_timestamps.get(client_id, 0.0)
                if now - last_alert >= self.debounce_seconds:
                    self._last_alert_timestamps[client_id] = now

                    # Package sample payloads and error details
                    samples = [rec.raw_payload for rec in list(window)[-3:]]
                    sample_errs = [rec.errors for rec in list(window)[-3:]]

                    alert = AnomalyAlert(
                        alert_id=f"ALERT_{uuid.uuid4().hex[:8].upper()}",
                        client_id=client_id,
                        failure_count=len(window),
                        window_seconds=self.window_seconds,
                        timestamp=now,
                        sample_payloads=samples,
                        sample_errors=sample_errs,
                    )

                    if self.alert_callback:
                        self.alert_callback(alert)

                    return alert

            return None

    def record_success(self, client_id: str) -> None:
        """
        Tracks a healthy transaction for this client.
        """
        with self._lock:
            self._total_successes[client_id] = self._total_successes.get(client_id, 0) + 1

    def build_anomaly_context(self, alert: AnomalyAlert) -> AnomalyContext:
        """
        Translates an AnomalyAlert into an actionable AnomalyContext for the Synthesizer Agent.
        """
        canonical_schema = CanonicalUPIPaymentRequest.model_json_schema()
        # Select the most recent failed payload as the archetype
        malformed_sample = alert.sample_payloads[-1] if alert.sample_payloads else {}
        validation_errors = alert.sample_errors[-1] if alert.sample_errors else []

        return AnomalyContext(
            client_id=alert.client_id,
            canonical_schema=canonical_schema,
            malformed_payload=malformed_sample,
            validation_errors=validation_errors,
        )

    def get_metrics(self) -> Dict[str, Any]:
        with self._lock:
            now = time.time()
            active_failure_rates = {}
            for cid, window in self._windows.items():
                cutoff = now - self.window_seconds
                active_count = sum(1 for rec in window if rec.timestamp >= cutoff)
                active_failure_rates[cid] = active_count

            return {
                "active_failure_bursts": active_failure_rates,
                "total_failures_by_bank": dict(self._total_failures),
                "total_successes_by_bank": dict(self._total_successes),
            }

    def reset_client(self, client_id: str) -> None:
        """
        Clears the sliding window failures and alert debounce timer for a specific client.
        Enables seamless repeatable testing.
        """
        with self._lock:
            if client_id in self._windows:
                self._windows[client_id].clear()
            if client_id in self._last_alert_timestamps:
                del self._last_alert_timestamps[client_id]

    def clear(self) -> None:
        with self._lock:
            self._windows.clear()
            self._last_alert_timestamps.clear()
            self._total_failures.clear()
            self._total_successes.clear()


# Global Scout Agent singleton
scout_agent = ScoutAgent()
