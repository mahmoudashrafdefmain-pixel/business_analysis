r"""
================================================================================
run_all_gatherings.py
--------------------------------------------------------------------------------
PURPOSE:
  Master script to run all 3 gathering scripts in sequence.
  Regenerates all datasets and combined versions 100% on D: disk.
================================================================================
"""

#& "D:\Python\Python312\python.exe" "D:\ecommerce_analytics_datasets\Gathring_Code\run_all_gatherings.py"

import os
import sys
import subprocess
import time

# Auto-detect and switch to Python 3.12 if invoked by MSYS2 Python
PYTHON_312 = r"D:\Python\Python312\python.exe"
if os.path.exists(PYTHON_312) and sys.executable.lower() != PYTHON_312.lower() and "msys2" in sys.executable.lower():
    print(f"[!] Detected MSYS2 environment ({sys.executable}).", flush=True)
    print(f"[>] Automatically redirecting to Python 3.12 ({PYTHON_312})...\n", flush=True)
    ret = subprocess.run([PYTHON_312, __file__] + sys.argv[1:])
    sys.exit(ret.returncode)

current_dir = os.path.dirname(os.path.abspath(__file__))
active_python = sys.executable

scripts = [
    ("01_gather_olist_ecommerce.py", "Olist Brazilian E-Commerce"),
    ("02_gather_global_superstore.py", "Global Superstore"),
    ("03_gather_uci_online_retail_ii.py", "UCI Online Retail II")
]

print("====================================================================")
print("       MASTER PIPELINE: GATHERING & COMBINING ALL 3 DATASETS        ")
print(f"       Using Python: {active_python}")
print("====================================================================\n")

start_all = time.time()

for script_name, label in scripts:
    script_path = os.path.join(current_dir, script_name)
    print(f"\n####################################################################")
    print(f"RUNNING: {label} ({script_name})")
    print(f"####################################################################")
    
    start_t = time.time()
    res = subprocess.run([active_python, script_path], check=True)
    elapsed = time.time() - start_t
    print(f"Completed in {elapsed:.1f} seconds.\n")

total_elapsed = time.time() - start_all
print("====================================================================")
print(f"ALL 3 DATASETS FULLY REGENERATED ON D: DISK IN {total_elapsed:.1f}s!")
print("====================================================================")
