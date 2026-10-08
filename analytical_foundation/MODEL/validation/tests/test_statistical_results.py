import pytest
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
VAL_DIR = BASE_DIR / "MODEL" / "validation"

def test_econometric_pricing_elasticity():
    p = VAL_DIR / "pricing_elasticity_loglog.parquet"
    assert p.exists(), "pricing_elasticity_loglog.parquet missing"
    df = pd.read_parquet(p)
    assert len(df) >= 3
    assert (df["elasticity_beta"] < 0).all(), "Pricing elasticity betas must be negative"

def test_discount_destruction_cliff():
    p = VAL_DIR / "discount_destruction_empirical.parquet"
    assert p.exists(), "discount_destruction_empirical.parquet missing"
    df = pd.read_parquet(p)
    assert len(df) == 6
    high_disc = df[df["discount_band"].isin(["21% - 30%", "31% - 50%", "51% - 85%"])]
    assert (high_disc["business_rule_recommendation"].str.contains("Hard-blocked")).all()
