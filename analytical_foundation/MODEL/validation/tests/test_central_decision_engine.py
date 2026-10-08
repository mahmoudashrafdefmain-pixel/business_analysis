"""
TEST CENTRAL DECISION ENGINE & BUSINESS RULES (Production Comprehensive Test Suite)
"""

import pytest
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(BASE_DIR / "MODEL" / "decision_engine"))

from decision_engine import decide_opportunity
from calculations import (
    search_products,
    get_recommended_price,
    compute_price_sensitivity,
    compute_budget_plan,
    compute_market_gaps
)

def test_decision_engine_high_volume_product():
    res = decide_opportunity("85123A", "United Kingdom", "uci_online_retail_ii")
    assert res["decision"] in ["ENTER", "TEST", "WATCH", "AVOID"]
    assert res["opportunity_score"] > 0
    assert "indicators" in res
    assert len(res["indicators"]) == 5
    assert "opportunity" in res["indicators"]
    assert "demand" in res["indicators"]
    assert "success_prob" in res["indicators"]
    assert "economics" in res["indicators"]
    assert "risk" in res["indicators"]
    assert len(res["action_checklist"]) <= 4
    assert "why_breakdown" in res
    assert len(res["why_breakdown"]["supports"]) > 0
    assert len(res["why_breakdown"]["hurts"]) > 0
    assert len(res["why_breakdown"]["final_reason"]) > 20

def test_decision_engine_cold_start():
    res = decide_opportunity("UNKNOWN_SPARSE_SKU_9999", "United States", "global_superstore")
    assert res["confidence"] == "Insufficient"
    assert "action_checklist" in res
    assert len(res["action_checklist"]) >= 1

def test_decision_engine_assumption_driven_economics():
    res = decide_opportunity(
        "85123A", 
        "United Kingdom", 
        "uci_online_retail_ii",
        assumptions={"unit_cost": 1.50}
    )
    assert res["metrics"]["assumed_cost"] == 1.50
    assert "Assumption" in res["metrics"]["economic_rating"]

def test_smart_product_search():
    results = search_products("clock", limit=10)
    assert len(results) > 0
    names = [r["product_name"].lower() for r in results]
    assert any("clock" in name for name in names)

def test_price_recommendations_and_sensitivity():
    price_info = get_recommended_price("85123A", "United Kingdom", city="London", dataset_key="uci_online_retail_ii")
    assert price_info["price_center"] > 0
    assert price_info["price_low"] < price_info["price_high"]
    assert price_info["currency_symbol"] in price_info["formatted_range"]
    
    sens = compute_price_sensitivity("85123A", "United Kingdom", dataset_key="uci_online_retail_ii")
    assert len(sens["curve_points"]) == 7
    assert sens["optimal_price"] > 0

def test_budget_plan_feasibility():
    plan_good = compute_budget_plan(10000.0, "85123A", "United Kingdom")
    assert plan_good["is_feasible"] is True
    assert plan_good["purchasable_units"] > 0
    
    plan_underfunded = compute_budget_plan(5.0, "85123A", "United Kingdom")
    assert plan_underfunded["is_feasible"] is False
    assert "Underfunded" in plan_underfunded["break_even_timeline"]

def test_market_gaps_computation():
    gaps = compute_market_gaps()
    assert "markets_summary" in gaps
    assert len(gaps["markets_summary"]) >= 5
    assert "product_market_matrix" in gaps
    assert not gaps["product_market_matrix"].empty

def test_all_four_rf_models():
    res_ol = decide_opportunity("aca2eb7d00ea1a7b8ebd4e68314663af", "Brazil", "olist")
    assert res_ol["decision"] in ["ENTER", "TEST", "WATCH", "AVOID"]
    
    res_gs = decide_opportunity("FUR-BO-10001798", "United States", "global_superstore")
    assert res_gs["decision"] in ["ENTER", "TEST", "WATCH", "AVOID"]
    
    res_uci = decide_opportunity("85123A", "United Kingdom", "uci_online_retail_ii")
    assert res_uci["decision"] in ["ENTER", "TEST", "WATCH", "AVOID"]
    
    res_comb = decide_opportunity("85123A", "United Kingdom", "all_datasets")
    assert res_comb["decision"] in ["ENTER", "TEST", "WATCH", "AVOID"]
