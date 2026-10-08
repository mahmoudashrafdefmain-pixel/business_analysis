"""
PRODUCT MARKET ENTRY DECISION PLATFORM
Root Application Entrypoint for Streamlit Community Cloud, Render, and Local Execution.
"""
import sys
from pathlib import Path

# Setup paths dynamically relative to repository root
ROOT_DIR = Path(__file__).parent.resolve()
APP_DIR = ROOT_DIR / "analytical_foundation" / "DASHBOARDS" / "app"
ENGINE_DIR = ROOT_DIR / "analytical_foundation" / "MODEL" / "decision_engine"

for p in [APP_DIR, ENGINE_DIR, ROOT_DIR]:
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

# Execute primary application entrypoint
main_script = APP_DIR / "main.py"
with open(main_script, "r", encoding="utf-8") as f:
    code = compile(f.read(), str(main_script), "exec")
    exec(code, globals())