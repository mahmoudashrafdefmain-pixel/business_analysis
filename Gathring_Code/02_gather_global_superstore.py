r"""
================================================================================
02_gather_global_superstore.py
--------------------------------------------------------------------------------
PURPOSE:
  1. Searches and downloads the Global Superstore dataset from Kaggle.
  2. Copies the raw files (CSV, XLSX, train.csv) to D:\ecommerce_analytics_datasets\02_global_superstore\
  3. Loads Global_Superstore2.csv into memory.
  4. Feature-engineers shipping durations, profit margins, and date hierarchies.
  5. Exports the combined analytical table: global_superstore_combined.csv
  
REPRODUCIBILITY:
  Even if you delete the folder D:\ecommerce_analytics_datasets\02_global_superstore,
  running this script will regenerate 100% of the raw tables and the combined table.
================================================================================
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

# Auto-detect and switch to Python 3.12 if invoked by MSYS2 Python
PYTHON_312 = r"D:\Python\Python312\python.exe"
if os.path.exists(PYTHON_312) and sys.executable.lower() != PYTHON_312.lower() and "msys2" in sys.executable.lower():
    print(f"[!] Detected MSYS2 environment ({sys.executable}).", flush=True)
    print(f"[>] Automatically redirecting to Python 3.12 ({PYTHON_312})...\n", flush=True)
    ret = subprocess.run([PYTHON_312, __file__] + sys.argv[1:])
    sys.exit(ret.returncode)

# 1. Ensure required packages are installed
for pkg in ["kagglehub", "pandas", "numpy", "openpyxl"]:
    try:
        __import__(pkg)
    except ImportError:
        print(f"[!] Package '{pkg}' not found. Installing via pip...", flush=True)
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

import kagglehub
import pandas as pd
import numpy as np

# 2. Target Output Directory
TARGET_DIR = str(Path(__file__).resolve().parents[1] / "02_global_superstore")
os.makedirs(TARGET_DIR, exist_ok=True)
print(f"[1/5] Target directory verified: {TARGET_DIR}", flush=True)

# 3. Search and Download from Kaggle
KAGGLE_DATASET_HANDLE = "apoorvaappz/global-super-store-dataset"
print(f"[2/5] Searching & downloading from Kaggle: '{KAGGLE_DATASET_HANDLE}'...", flush=True)
cached_path = kagglehub.dataset_download(KAGGLE_DATASET_HANDLE)
print(f"[OK] Downloaded and cached at: {cached_path}", flush=True)

# 4. Copy raw files into target folder
print("[3/5] Copying raw files to D: disk...", flush=True)
for fname in os.listdir(cached_path):
    src_file = os.path.join(cached_path, fname)
    dst_file = os.path.join(TARGET_DIR, fname)
    if os.path.isfile(src_file):
        shutil.copy2(src_file, dst_file)
        print(f"  -> Saved: {fname} ({os.path.getsize(dst_file):,} bytes)", flush=True)

# 5. Load and Process Global Superstore
print("\n[4/5] Loading and feature-engineering Global Superstore...", flush=True)
raw_csv_path = os.path.join(TARGET_DIR, "Global_Superstore2.csv")
df_gs = pd.read_csv(raw_csv_path, encoding="latin1")

# Feature Engineering
df_gs["Order Date"] = pd.to_datetime(df_gs["Order Date"], dayfirst=True)
df_gs["Ship Date"] = pd.to_datetime(df_gs["Ship Date"], dayfirst=True)
df_gs["Shipping Days"] = (df_gs["Ship Date"] - df_gs["Order Date"]).dt.days
df_gs["Profit Margin"] = df_gs["Profit"] / df_gs["Sales"].replace(0, np.nan)
df_gs["Order Year"] = df_gs["Order Date"].dt.year
df_gs["Order Month"] = df_gs["Order Date"].dt.month
df_gs["Order Year_Month"] = df_gs["Order Date"].dt.to_period("M").astype(str)

# 6. Save Combined Table
out_combined_file = os.path.join(TARGET_DIR, "global_superstore_combined.csv")
print(f"\n[5/5] Exporting combined analytical table to: {out_combined_file}...", flush=True)
df_gs.to_csv(out_combined_file, index=False)

print(f"\n[SUCCESS] Global Superstore dataset is 100% complete!")
print(f"Combined file shape: {df_gs.shape[0]:,} rows x {df_gs.shape[1]} columns")
print(f"Combined file size : {os.path.getsize(out_combined_file)/(1024*1024):.2f} MB")
