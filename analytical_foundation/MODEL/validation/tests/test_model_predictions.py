import pytest
import joblib
import numpy as np
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
MODELS_DIR = BASE_DIR / "MODEL" / "models"

def test_cross_dataset_model_inference():
    p = MODELS_DIR / "cross_dataset_success_model.joblib"
    assert p.exists(), "cross_dataset_success_model.joblib missing"
    model = joblib.load(p)
    sample_df = pd.DataFrame([{
        "norm_unit_price_pct": 0.5,
        "rel_price_vs_category": 1.0,
        "norm_velocity_pct": 0.5,
        "customer_repeat_rate": 0.1,
        "norm_freight_burden": 0.2,
        "norm_discount_rate": 0.05,
        "profit_available": 1,
        "discount_available": 1,
        "shipping_cost_available": 1
    }])
    pred_prob = model.predict_proba(sample_df)
    assert pred_prob.shape == (1, 2)
    assert 0.0 <= pred_prob[0, 1] <= 1.0

def test_gs_profitability_classifier_inference():
    p = MODELS_DIR / "gs_profitability_classifier.joblib"
    assert p.exists(), "gs_profitability_classifier.joblib missing"
    model = joblib.load(p)
    row = {
        "Sales": 250.0, "Quantity": 3, "Discount": 0.15, "Shipping_Cost": 25.0,
        "shipping_ratio": 0.10, "unit_price": 83.33, "Shipping_Days": 4.0,
        "Order_Month": 8, "Order_DayOfWeek": 3,
        "market_Africa": 0, "market_Canada": 0, "market_EMEA": 0, "market_EU": 0, "market_LATAM": 0, "market_US": 1,
        "segment_Corporate": 0, "segment_Home_Office": 0,
        "cat_Office_Supplies": 0, "cat_Technology": 1
    }
    df_sample = pd.DataFrame([row])
    prob = model.predict_proba(df_sample)[0, 1]
    assert 0.0 <= prob <= 1.0
