"""
AUTOMATED GLOBAL DEPENDENCY & CASCADE AUDIT TESTS (Sections 214-215)
Verifies that changing Product, Price, Market, or Budget alters model feature vectors,
probabilities, and feasibility metrics mathematically.
"""

import pytest
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(BASE_DIR / "MODEL" / "decision_engine"))

from calculations import (
    compute_product_metrics,
    get_recommended_price,
    compute_price_sensitivity,
    compute_budget_plan
)
from decision_engine import decide_opportunity

def test_price_input_alters_model_probability_and_economics():
    """Verify that changing price directly alters model prediction and economics."""
    res_base = decide_opportunity("85123A", "United States", "all_datasets", assumptions={"price": 3.50})
    res_high = decide_opportunity("85123A", "United States", "all_datasets", assumptions={"price": 45.0})
    
    # Unit prices must differ
    assert res_base["metrics"]["avg_price"] == 3.50
    assert res_high["metrics"]["avg_price"] == 45.0
    
    # Price-dependent revenue must differ
    assert res_base["metrics"]["revenue"] != res_high["metrics"]["revenue"]
    
    # Model success probabilities must respond to price shift
    assert res_base["success_probability"] != res_high["success_probability"]
    assert res_base["success_probability"] > res_high["success_probability"]

def test_market_and_city_input_alters_price_corridor():
    """Verify that changing market and city applies geographic multipliers."""
    price_us = get_recommended_price("85123A", "United States")
    price_br = get_recommended_price("85123A", "Brazil")
    price_nyc = get_recommended_price("85123A", "United States", city="New York")
    
    # Brazil multiplier is lower than US multiplier
    assert price_us["price_center"] > price_br["price_center"]
    
    # NYC city multiplier (1.12) is higher than US base (1.05)
    assert price_nyc["price_center"] > price_us["price_center"]
    assert price_nyc["evidence_level"] == "City-level pricing"

def test_budget_input_alters_feasibility_and_timeline():
    """Verify that changing budget shifts feasibility from underfunded to feasible."""
    plan_small = compute_budget_plan(100.0, "85123A", "United States")
    plan_large = compute_budget_plan(15000.0, "85123A", "United States")
    
    assert plan_small["is_feasible"] is False
    assert plan_large["is_feasible"] is True
    assert "Underfunded" in plan_small["break_even_timeline"]
    assert "Months" in plan_large["break_even_timeline"]
    assert plan_large["purchasable_units"] > plan_small["purchasable_units"]

def test_dataset_scope_selects_dedicated_rf_model():
    """Verify that dataset scope routes to the correct dedicated RF model."""
    res_ol = decide_opportunity("aca2eb7d00ea1a7b8ebd4e68314663af", "Brazil", "olist")
    res_gs = decide_opportunity("OFF-AR-10003651", "United States", "global_superstore")
    res_uci = decide_opportunity("85123A", "United Kingdom", "uci_online_retail_ii")
    
    assert "Olist" in res_ol["how_calculated"]["model"]
    assert "Global Superstore" in res_gs["how_calculated"]["model"]
    assert "UCI Online Retail" in res_uci["how_calculated"]["model"]
