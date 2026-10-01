"""
Configuration and Environment Settings for DPI-Heal
Supports Multi-Provider LLMs (OpenAI, Gemini, Anthropic, Groq, Ollama / Local vLLM)
"""

import os
from typing import Optional
from dotenv import load_dotenv
from pydantic import BaseModel, Field

# Automatically load .env file if present
load_dotenv()


class Settings(BaseModel):
    # Gateway Server Settings
    GATEWAY_HOST: str = Field(default="127.0.0.1", description="FastAPI bind host")
    GATEWAY_PORT: int = Field(default=8000, description="FastAPI bind port")
    GATEWAY_TITLE: str = "DPI-Heal UPI Gateway"
    GATEWAY_VERSION: str = "1.0.0"

    # Scout Telemetry Settings
    SCOUT_FAILURE_THRESHOLD: int = Field(
        default=5,
        description="Number of validation failures within window to trigger healing alert",
    )
    SCOUT_WINDOW_SECONDS: float = Field(
        default=10.0,
        description="Sliding window duration in seconds for error burst velocity calculation",
    )
    SCOUT_DEBOUNCE_SECONDS: float = Field(
        default=5.0,
        description="Minimum quiet time between alerts for the same client_id",
    )

    # Multi-Provider LLM Synthesizer Settings
    LLM_PROVIDER: str = Field(
        default_factory=lambda: os.getenv("LLM_PROVIDER", "auto").lower(),
        description="LLM provider: 'auto', 'openai', 'gemini', 'anthropic', 'groq', 'ollama', or 'local'",
    )
    LLM_MODEL: str = Field(
        default_factory=lambda: os.getenv("LLM_MODEL", ""),
        description="Target model name (e.g. 'gpt-4o-mini', 'gemini-1.5-flash', 'llama-3.3-70b-versatile', 'llama3.2')",
    )
    OPENAI_API_KEY: Optional[str] = Field(
        default_factory=lambda: os.getenv("OPENAI_API_KEY", None),
        description="API key for OpenAI",
    )
    GEMINI_API_KEY: Optional[str] = Field(
        default_factory=lambda: os.getenv("GEMINI_API_KEY", None),
        description="API key for Google Gemini",
    )
    ANTHROPIC_API_KEY: Optional[str] = Field(
        default_factory=lambda: os.getenv("ANTHROPIC_API_KEY", None),
        description="API key for Anthropic Claude",
    )
    GROQ_API_KEY: Optional[str] = Field(
        default_factory=lambda: os.getenv("GROQ_API_KEY", None),
        description="API key for Groq",
    )
    LLM_BASE_URL: Optional[str] = Field(
        default_factory=lambda: os.getenv("LLM_BASE_URL", None),
        description="Base URL for local/custom OpenAI-compatible endpoints (e.g. http://localhost:11434/v1 for Ollama)",
    )
    LLM_TEMPERATURE: float = Field(
        default=0.0,
        description="Sampling temperature for LLM code synthesis (0.0 for maximum determinism)",
    )
    LLM_TIMEOUT: float = Field(
        default=15.0,
        description="Timeout in seconds for LLM generation requests",
    )
    ALLOW_OFFLINE_SYNTHESIS: bool = Field(
        default=True,
        description="Whether to fall back to deterministic AST/semantic heuristic synthesizer when offline or on failure",
    )

    # Formal Verifier & Safety Settings
    MAX_ADAPTER_EXECUTION_TIME_MS: float = Field(
        default=50.0,
        description="Maximum execution time allowed for adapter sandbox dry-run",
    )
    STRICT_Z3_VERIFICATION: bool = Field(
        default=True,
        description="Whether to run SMT solver invariant proof for monetary conservation",
    )

    # Cryptographic Audit Ledger Settings
    LEDGER_DIFFICULTY: int = Field(
        default=2,
        description="Proof-of-work difficulty prefix zeros for tamper-evident block sealing",
    )


# Singleton settings instance
settings = Settings()
