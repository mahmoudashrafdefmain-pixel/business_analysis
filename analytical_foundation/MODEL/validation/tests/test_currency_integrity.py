import pytest
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
DATA_DIR = BASE_DIR / "DATASETS" / "DATASETS_AFTER"

def test_native_currency_preservation():
    df_ol = pd.read_parquet(DATA_DIR / "olist_cleaned.parquet")
    assert (df_ol["native_currency"] == "BRL").all(), "Olist currency must be strictly BRL"
    
    df_gs = pd.read_parquet(DATA_DIR / "global_superstore_cleaned.parquet")
    assert (df_gs["native_currency"] == "USD").all(), "Global Superstore currency must be strictly USD"
    
    df_uci = pd.read_parquet(DATA_DIR / "online_retail_ii_cleaned.parquet")
    assert (df_uci["native_currency"] == "GBP").all(), "UCI currency must be strictly GBP"

def test_fx_conversion_audit():
    df_ol = pd.read_parquet(DATA_DIR / "olist_cleaned.parquet")
    assert (df_ol["fx_rate"] == 0.2857).all(), "Olist BRL FX rate must be 0.2857"
    
    df_uci = pd.read_parquet(DATA_DIR / "online_retail_ii_cleaned.parquet")
    assert (df_uci["fx_rate"] == 1.5500).all(), "UCI GBP FX rate must be 1.5500"

def test_no_raw_currency_blending_in_master():
    df_cat = pd.read_parquet(DATA_DIR / "product_market_reconciled.parquet")
    currencies = set(df_cat["native_currency"].unique())
    assert currencies == {"USD", "BRL", "GBP"}, f"Expected USD, BRL, GBP currencies, got {currencies}"
