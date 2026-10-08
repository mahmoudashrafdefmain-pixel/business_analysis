"""
OFFICIAL TEST SUITE LAUNCHER
Executes the full 29-test automated validation suite covering:
- Currency integrity & no-blending rules
- Clean data integrity across Olist, Global Superstore, and UCI
- Feature leakage prevention
- Global AppState input dependency & cascade verification
- Calibrated probability checks & econometric elasticity curves
"""
import sys
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
TEST_DIR = ROOT_DIR / "MODEL" / "validation" / "tests"

print("=" * 70)
print("  EXECUTING FULL 29-TEST AUTOMATED VALIDATION SUITE")
print(f"  Target: {TEST_DIR}")
print("=" * 70)

cmd = [
    sys.executable,
    "-m",
    "pytest",
    str(TEST_DIR),
    "-v",
    "-p",
    "no:cacheprovider"
]

res = subprocess.run(cmd, cwd=str(ROOT_DIR))
sys.exit(res.returncode)
