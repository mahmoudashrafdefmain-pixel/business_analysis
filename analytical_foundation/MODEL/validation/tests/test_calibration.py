import pytest
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
REGISTRY_DIR = BASE_DIR / "MODEL" / "model_registry"

def test_model_registry_calibration_scores():
    p = REGISTRY_DIR / "model_registry.parquet"
    assert p.exists(), "model_registry.parquet missing"
    df = pd.read_parquet(p)
    classifiers = df[df["task_type"] == "Binary Classification"]
    assert len(classifiers) > 0
    for _, row in classifiers.iterrows():
        brier = row.get("brier_score")
        if pd.notna(brier):
            assert 0.0 <= brier <= 0.25, f"High Brier score loss in {row['model_id']}: {brier}"
