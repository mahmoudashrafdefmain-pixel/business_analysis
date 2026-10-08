r"""
================================================================================
03_gather_uci_online_retail_ii.py
--------------------------------------------------------------------------------
PURPOSE:
  1. Searches and streams the Online Retail II archive from the UCI ML Repository.
  2. Saves online_retail_ii.zip in D:\ecommerce_analytics_datasets\03_online_retail_ii_uci\
  3. Extracts the 2-year Excel workbook (online_retail_II.xlsx).
  4. Reads both transactional sheets ("Year 2009-2010" and "Year 2010-2011").
  5. Concatenates them into a single 2-year master dataset (1,067,371 rows).
  6. Feature-engineers cancellations, total amounts, and calendar periods.
  7. Exports the combined master table: online_retail_ii_combined.csv
  
REPRODUCIBILITY:
  Even if you delete the folder D:\ecommerce_analytics_datasets\03_online_retail_ii_uci,
  running this script will regenerate 100% of the raw files and the combined table.
================================================================================
"""

import os
import sys
import shutil
import urllib.request
import zipfile
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
for pkg in ["pandas", "numpy", "openpyxl"]:
    try:
        __import__(pkg)
    except ImportError:
        print(f"[!] Package '{pkg}' not found. Installing via pip...", flush=True)
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

import pandas as pd
import numpy as np

# 2. Target Output Directory
TARGET_DIR = str(Path(__file__).resolve().parents[1] / "03_online_retail_ii_uci")
os.makedirs(TARGET_DIR, exist_ok=True)
print(f"[1/5] Target directory verified: {TARGET_DIR}", flush=True)

# 3. Stream & Download from UCI ML Repository
UCI_ZIP_URL = "https://archive.ics.uci.edu/static/public/502/online+retail+ii.zip"
zip_path = os.path.join(TARGET_DIR, "online_retail_ii.zip")

print(f"[2/5] Downloading from UCI: {UCI_ZIP_URL} ...", flush=True)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
req = urllib.request.Request(UCI_ZIP_URL, headers=headers)

with urllib.request.urlopen(req, timeout=180) as resp:
    with open(zip_path, "wb") as out_f:
        shutil.copyfileobj(resp, out_f)
print(f"[OK] Downloaded archive: {os.path.getsize(zip_path):,} bytes", flush=True)

# 4. Extract the Excel Workbook
print("[3/5] Extracting online_retail_II.xlsx from ZIP archive...", flush=True)
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(TARGET_DIR)
print(f"[OK] Extracted files: {os.listdir(TARGET_DIR)}", flush=True)

# 5. Read Sheets and Concatenate into 2-Year Master
xlsx_path = os.path.join(TARGET_DIR, "online_retail_II.xlsx")
print("\n[4/5] Reading and combining Excel sheets into unified table...", flush=True)

print("  - Reading Sheet 'Year 2009-2010'...", flush=True)
df_y1 = pd.read_excel(xlsx_path, sheet_name="Year 2009-2010")
df_y1["Dataset_Period"] = "2009-2010"
print(f"    Loaded {df_y1.shape[0]:,} rows", flush=True)

print("  - Reading Sheet 'Year 2010-2011'...", flush=True)
df_y2 = pd.read_excel(xlsx_path, sheet_name="Year 2010-2011")
df_y2["Dataset_Period"] = "2010-2011"
print(f"    Loaded {df_y2.shape[0]:,} rows", flush=True)

print("  - Concatenating sheets into unified DataFrame...", flush=True)
df_uci_combined = pd.concat([df_y1, df_y2], ignore_index=True)

print("  - Engineering business features...", flush=True)
df_uci_combined["InvoiceDate"] = pd.to_datetime(df_uci_combined["InvoiceDate"])
df_uci_combined["Is_Cancellation"] = df_uci_combined["Invoice"].astype(str).str.startswith("C").astype(int)
df_uci_combined["Total_Amount"] = df_uci_combined["Quantity"] * df_uci_combined["Price"]
df_uci_combined["Order_Year"] = df_uci_combined["InvoiceDate"].dt.year
df_uci_combined["Order_Month"] = df_uci_combined["InvoiceDate"].dt.month
df_uci_combined["Order_Year_Month"] = df_uci_combined["InvoiceDate"].dt.to_period("M").astype(str)

# 6. Save Combined Master Table
out_combined_file = os.path.join(TARGET_DIR, "online_retail_ii_combined.csv")
print(f"\n[5/5] Exporting combined master table to: {out_combined_file} ...", flush=True)
df_uci_combined.to_csv(out_combined_file, index=False)

print(f"\n[SUCCESS] UCI Online Retail II dataset is 100% complete!")
print(f"Combined file shape: {df_uci_combined.shape[0]:,} rows x {df_uci_combined.shape[1]} columns")
print(f"Combined file size : {os.path.getsize(out_combined_file)/(1024*1024):.2f} MB")
