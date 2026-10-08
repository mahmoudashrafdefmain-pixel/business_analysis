import pytest
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
DATA_DIR = BASE_DIR / "DATASETS" / "DATASETS_AFTER"

def test_olist_temporal_chronology():
    df = pd.read_parquet(DATA_DIR / "olist_cleaned.parquet")
    dates = pd.to_datetime(df["order_purchase_timestamp"]).dropna()
    assert dates.min() >= pd.Timestamp("2016-01-01")
    assert dates.max() <= pd.Timestamp("2018-12-31")

def test_superstore_temporal_chronology():
    df = pd.read_parquet(DATA_DIR / "global_superstore_cleaned.parquet")
    dates = pd.to_datetime(df["Order Date"]).dropna()
    assert dates.min() >= pd.Timestamp("2011-01-01")
    assert dates.max() <= pd.Timestamp("2014-12-31")

def test_uci_temporal_chronology():
    df = pd.read_parquet(DATA_DIR / "online_retail_ii_cleaned.parquet")
    dates = pd.to_datetime(df["InvoiceDate"]).dropna()
    assert dates.min() >= pd.Timestamp("2009-12-01")
    assert dates.max() <= pd.Timestamp("2011-12-31")
