"""
OFFICIAL APPLICATION LAUNCHER (Section 75)
Starts the single unified web application containing both Static and Dynamic modes.
"""
import sys
import subprocess
from pathlib import Path

LAUNCHER_DIR = Path(__file__).parent.resolve()
APP_DIR = LAUNCHER_DIR.parent / "app"
MAIN_SCRIPT = APP_DIR / "main.py"

print("=" * 70)
print("  LAUNCHING PRODUCT MARKET ENTRY DECISION PLATFORM")
print(f"  Target: {MAIN_SCRIPT}")
print("=" * 70)

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
    subprocess.run(cmd)
except KeyboardInterrupt:
    print("\nPlatform shut down cleanly.")
