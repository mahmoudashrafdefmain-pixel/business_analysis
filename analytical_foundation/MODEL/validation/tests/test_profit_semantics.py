import pytest
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
DATA_DIR = BASE_DIR / "DATASETS" / "DATASETS_AFTER"

def test_profit_semantics_isolation():
    df_cat = pd.read_parquet(DATA_DIR / "product_market_reconciled.parquet")
    
    gs_items = df_cat[df_cat["dataset_source"] == "global_superstore"]
    assert gs_items["profit_status"].str.contains("AUDITED ACTUAL").all(), "Global Superstore profit must be AUDITED ACTUAL"
    assert gs_items["native_profit"].notna().sum() > 0, "GS must have non-null profit values"
    
    ol_items = df_cat[df_cat["dataset_source"] == "olist"]
    assert ol_items["profit_status"].str.contains("MARKETPLACE COMMISSION MODEL").all(), "Olist profit must follow audited 15% marketplace commission model"
    assert ol_items["native_profit"].notna().all(), "Olist native_profit must be fully populated (zero nulls)"
    
    uci_items = df_cat[df_cat["dataset_source"] == "uci_online_retail_ii"]
    assert uci_items["profit_status"].str.contains("WHOLESALE DISTRIBUTOR MODEL").all(), "UCI profit must follow audited 22% wholesale markup model"
    assert uci_items["native_profit"].notna().all(), "UCI native_profit must be fully populated (zero nulls)"
