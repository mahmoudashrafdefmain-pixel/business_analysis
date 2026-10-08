"""
LAUNCHER: STATIC EXECUTIVE MARKET INTELLIGENCE DASHBOARD
Starts the application directly into Static Executive Mode.
"""
import sys
import os
import subprocess
from pathlib import Path

LAUNCHER_DIR = Path(__file__).parent.resolve()
MAIN_SCRIPT = LAUNCHER_DIR.parent / "app" / "main.py"

print("=" * 70)
print("  LAUNCHING STATIC EXECUTIVE MARKET INTELLIGENCE DASHBOARD")
print("=" * 70)

env = os.environ.copy()
env["APP_INITIAL_MODE"] = "STATIC"

cmd = [
    sys.executable,
    "-m",
    "streamlit",
    "run",
    str(MAIN_SCRIPT),
    "--server.port",
    "8501",
    "--server.headless",
    "false"
]

try:
    subprocess.run(cmd, env=env)
except KeyboardInterrupt:
    print("\nStatic dashboard shut down cleanly.")