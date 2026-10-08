r"""
================================================================================
01_gather_olist_ecommerce.py
--------------------------------------------------------------------------------
PURPOSE:
  1. Searches and downloads the Olist Brazilian E-Commerce dataset from Kaggle.
  2. Copies all 9 raw relational CSV tables to D:\ecommerce_analytics_datasets\01_brazilian_ecommerce_olist\
  3. Loads and performs a 360-degree relational merge of all tables.
  4. Feature-engineers delivery SLAs, order values, delays, and calendar features.
  5. Exports the master analytical combined table: olist_master_combined.csv
  
REPRODUCIBILITY:
  Even if you delete the folder D:\ecommerce_analytics_datasets\01_brazilian_ecommerce_olist,
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
for pkg in ["kagglehub", "pandas", "numpy"]:
    try:
        __import__(pkg)
    except ImportError:
        print(f"[!] Package '{pkg}' not found. Installing via pip...", flush=True)
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

import kagglehub
import pandas as pd
import numpy as np

# 2. Target Output Directory
TARGET_DIR = str(Path(__file__).resolve().parents[1] / "01_brazilian_ecommerce_olist")
os.makedirs(TARGET_DIR, exist_ok=True)
print(f"[1/5] Target directory verified: {TARGET_DIR}", flush=True)

# 3. Search and Download from Kaggle
KAGGLE_DATASET_HANDLE = "olistbr/brazilian-ecommerce"
print(f"[2/5] Searching & downloading from Kaggle: '{KAGGLE_DATASET_HANDLE}'...", flush=True)
cached_path = kagglehub.dataset_download(KAGGLE_DATASET_HANDLE)
print(f"[OK] Downloaded and cached at: {cached_path}", flush=True)

# 4. Copy all 9 raw CSV files into target folder
print("[3/5] Copying raw relational tables to D: disk...", flush=True)
for fname in os.listdir(cached_path):
    src_file = os.path.join(cached_path, fname)
    dst_file = os.path.join(TARGET_DIR, fname)
    if os.path.isfile(src_file) and fname.endswith(".csv"):
        shutil.copy2(src_file, dst_file)
        print(f"  -> Saved: {fname} ({os.path.getsize(dst_file):,} bytes)", flush=True)

# 5. Load and Merge all Relational Tables into Combined Master
print("\n[4/5] Loading raw relational tables into memory...", flush=True)
orders = pd.read_csv(os.path.join(TARGET_DIR, "olist_orders_dataset.csv"))
items = pd.read_csv(os.path.join(TARGET_DIR, "olist_order_items_dataset.csv"))
customers = pd.read_csv(os.path.join(TARGET_DIR, "olist_customers_dataset.csv"))
products = pd.read_csv(os.path.join(TARGET_DIR, "olist_products_dataset.csv"))
sellers = pd.read_csv(os.path.join(TARGET_DIR, "olist_sellers_dataset.csv"))
payments = pd.read_csv(os.path.join(TARGET_DIR, "olist_order_payments_dataset.csv"))
reviews = pd.read_csv(os.path.join(TARGET_DIR, "olist_order_reviews_dataset.csv"))
translation = pd.read_csv(os.path.join(TARGET_DIR, "product_category_name_translation.csv"))

# Map category translations
print("  - Merging product category translations...", flush=True)
products = products.merge(translation, on="product_category_name", how="left")
products["product_category_name_english"] = products["product_category_name_english"].fillna(products["product_category_name"]).fillna("unknown")

# Aggregate payments by order_id
print("  - Aggregating payment transactions...", flush=True)
payments_sorted = payments.sort_values(by=["order_id", "payment_value"], ascending=[True, False])
primary_payment = payments_sorted.drop_duplicates(subset=["order_id"])[["order_id", "payment_type", "payment_installments"]]
payment_totals = payments.groupby("order_id")["payment_value"].sum().reset_index().rename(columns={"payment_value": "total_payment_value"})
payments_agg = primary_payment.merge(payment_totals, on="order_id", how="left")

# Aggregate reviews by order_id
print("  - Aggregating customer review ratings...", flush=True)
reviews_agg = reviews.groupby("order_id").agg(review_score=("review_score", "mean")).reset_index()

# Merge all tables
print("  - Executing multi-table relational join...", flush=True)
olist_master = items.merge(orders, on="order_id", how="left")
olist_master = olist_master.merge(customers, on="customer_id", how="left")
olist_master = olist_master.merge(products, on="product_id", how="left")
olist_master = olist_master.merge(sellers, on="seller_id", how="left")
olist_master = olist_master.merge(payments_agg, on="order_id", how="left")
olist_master = olist_master.merge(reviews_agg, on="order_id", how="left")

# Feature engineering
print("  - Engineering delivery SLA and calendar features...", flush=True)
olist_master["order_purchase_timestamp"] = pd.to_datetime(olist_master["order_purchase_timestamp"])
olist_master["order_delivered_customer_date"] = pd.to_datetime(olist_master["order_delivered_customer_date"])
olist_master["order_estimated_delivery_date"] = pd.to_datetime(olist_master["order_estimated_delivery_date"])

olist_master["total_item_value"] = (olist_master["price"] + olist_master["freight_value"]).round(2)
olist_master["actual_delivery_days"] = ((olist_master["order_delivered_customer_date"] - olist_master["order_purchase_timestamp"]).dt.total_seconds() / 86400.0).round(2)
olist_master["estimated_delivery_days"] = ((olist_master["order_estimated_delivery_date"] - olist_master["order_purchase_timestamp"]).dt.total_seconds() / 86400.0).round(2)

raw_delay = (olist_master["order_delivered_customer_date"] - olist_master["order_estimated_delivery_date"]).dt.total_seconds() / 86400.0
olist_master["days_late"] = np.where(raw_delay > 0, raw_delay, 0.0).round(2)
olist_master["days_early"] = np.where(raw_delay < 0, np.abs(raw_delay), 0.0).round(2)

conditions = [
    olist_master["order_delivered_customer_date"].isna(),
    raw_delay > 0,
    raw_delay == 0,
    raw_delay < 0
]
choices = ["Not Delivered", "Delayed", "On Time", "Delivered Early"]
olist_master["delivery_status"] = np.select(conditions, choices, default="Unknown")
olist_master["is_delayed"] = np.where(raw_delay > 0, 1, 0)

olist_master["order_year"] = olist_master["order_purchase_timestamp"].dt.year
olist_master["order_month"] = olist_master["order_purchase_timestamp"].dt.month
olist_master["order_year_month"] = olist_master["order_purchase_timestamp"].dt.to_period("M").astype(str)

# Format dates cleanly
date_cols = [
    "shipping_limit_date",
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]
for col in date_cols:
    olist_master[col] = pd.to_datetime(olist_master[col]).dt.strftime("%Y-%m-%d %H:%M:%S").fillna("")

# 6. Save Combined Master Tables (CSV and formatted XLSX)
out_combined_csv = os.path.join(TARGET_DIR, "olist_master_combined.csv")
out_combined_xlsx = os.path.join(TARGET_DIR, "olist_master_combined.xlsx")

print(f"\n[5/5] Exporting clean master CSV to: {out_combined_csv}...", flush=True)
olist_master.to_csv(out_combined_csv, index=False)
print(f"[OK] Master CSV saved: {olist_master.shape[0]:,} rows x {olist_master.shape[1]} columns", flush=True)

print(f"Exporting Auto-Fitted Excel XLSX to: {out_combined_xlsx}...", flush=True)
with pd.ExcelWriter(out_combined_xlsx, engine="xlsxwriter") as writer:
    olist_master.to_excel(writer, sheet_name="Master_Data", index=False)
    ws = writer.sheets["Master_Data"]
    for i, col in enumerate(olist_master.columns):
        if "id" in col:
            w = 35
        elif "date" in col or "timestamp" in col:
            w = 22
        elif "name" in col or "city" in col:
            w = 28
        else:
            w = max(len(col), 14) + 4
        ws.set_column(i, i, w)
    ws.freeze_panes(1, 0)

print(f"[OK] Master XLSX saved: {os.path.getsize(out_combined_xlsx)/(1024*1024):.2f} MB")
print(f"\n[SUCCESS] Olist Brazilian E-Commerce dataset is 100% complete and Excel-ready with ZERO ###!")
