"""
Project DPI-Heal: Main Execution Gateway & Simulation CLI
Autonomous Self-Healing Middleware Swarm for Digital Public Infrastructure
"""

import argparse
import sys

# Ensure clean UTF-8 console output on Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from core.config import settings


def parse_args():
    parser = argparse.ArgumentParser(
        description="Project DPI-Heal: Autonomous Self-Healing Middleware Swarm"
    )
    parser.add_argument(
        "--simulate",
        action="store_true",
        help="Run the complete end-to-end synthetic bank traffic & autonomous self-healing simulation (Default).",
    )
    parser.add_argument(
        "--serve",
        action="store_true",
        help="Launch the live FastAPI Gateway server using Uvicorn.",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run the comprehensive pytest test suite.",
    )
    parser.add_argument(
        "--host",
        type=str,
        default=settings.GATEWAY_HOST,
        help=f"Host interface to bind server (default: {settings.GATEWAY_HOST})",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=settings.GATEWAY_PORT,
        help=f"Port to bind server (default: {settings.GATEWAY_PORT})",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if args.serve:
        import uvicorn
        print(f"Starting DPI-Heal Gateway Server on {args.host}:{args.port}...")
        uvicorn.run("gateway.server:app", host=args.host, port=args.port, reload=False)
        return 0

    if args.test:
        import pytest
        print("Executing DPI-Heal Test Suite via pytest...")
        exit_code = pytest.main(["-v", "tests/test_swarm.py"])
        return int(exit_code)

    # Default action: Run the simulation demonstration
    from tests.mock_banks import run_simulation
    success = run_simulation()
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
