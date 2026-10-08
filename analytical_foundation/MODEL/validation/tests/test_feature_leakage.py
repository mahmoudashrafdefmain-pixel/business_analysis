import pytest
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
VAL_DIR = BASE_DIR / "MODEL" / "validation"

def test_leakage_audit_suite_results_pass():
    p = VAL_DIR / "leakage_audit_suite_results.parquet"
    assert p.exists(), "leakage_audit_suite_results.parquet missing"
    df = pd.read_parquet(p)
    assert len(df) == 8, f"Expected 8 tests in leakage audit suite, got {len(df)}"
    for _, row in df.iterrows():
        assert "PASS" in row["leakage_flag"], f"Leakage test {row['test_name']} failed with flag {row['leakage_flag']}"
