import pytest
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
DATA_DIR = BASE_DIR / "DATASETS" / "DATASETS_AFTER"

def test_olist_data_integrity():
    p = DATA_DIR / "olist_cleaned.parquet"
    assert p.exists(), "olist_cleaned.parquet missing"
    df = pd.read_parquet(p)
    assert len(df) == 112650, f"Expected 112,650 rows in Olist, got {len(df)}"
    assert "is_delayed" in df.columns
    assert "freight_value" in df.columns
    assert "price" in df.columns
    assert df["product_category_name_english"].notna().all(), "Olist category must have zero nulls"
    assert df["product_weight_g"].notna().all(), "Olist weight must have zero nulls"
    assert df["review_score"].notna().all(), "Olist reviews must have zero nulls"
    assert df["native_profit"].notna().all(), "Olist native_profit must have zero nulls"

def test_global_superstore_data_integrity():
    p = DATA_DIR / "global_superstore_cleaned.parquet"
    assert p.exists(), "global_superstore_cleaned.parquet missing"
    df = pd.read_parquet(p)
    assert len(df) == 51290, f"Expected 51,290 rows in Superstore, got {len(df)}"
    assert "Sales" in df.columns
    assert "Profit" in df.columns
    assert "Discount" in df.columns
    assert df["Postal Code"].notna().all(), "Global Superstore Postal Code must have zero nulls"
    assert df["Postal Code"].astype(str).str.strip().ne("").all(), "Zero empty postal codes"

def test_uci_data_integrity():
    p = DATA_DIR / "online_retail_ii_cleaned.parquet"
    assert p.exists(), "online_retail_ii_cleaned.parquet missing"
    df = pd.read_parquet(p)
    assert len(df) == 1067371, f"Expected 1,067,371 rows in UCI, got {len(df)}"
    assert "Total_Amount" in df.columns
    assert "is_valid_sale" in df.columns
    assert df["Customer ID"].notna().all(), "UCI Customer ID must have zero nulls"
    assert df["Description"].notna().all(), "UCI Description must have zero nulls"
    assert df["native_profit"].notna().all(), "UCI native_profit must have zero nulls"

def test_product_master_unified_integrity():
    p = DATA_DIR / "product_market_reconciled.parquet"
    assert p.exists(), "product_market_reconciled.parquet missing"
    df = pd.read_parquet(p)
    assert len(df) >= 47417, f"Expected at least 47,417 items, got {len(df)}"
    assert df["category"].notna().all(), "Zero null categories in unified product master"
    assert (df["category"].str.lower() != "unknown").all(), "Zero 'unknown' product categories"
    assert (df["category"].str.lower() != "undefined").all(), "Zero 'undefined' product categories"
    assert df["native_profit"].notna().all(), "Zero null native profits across catalog"
