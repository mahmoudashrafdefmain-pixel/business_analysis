"""
GLOBAL APPLICATION STATE & CASCADE RECALCULATION ENGINE (Sections 176-180, 221)
Single Authoritative Source of Truth.
Every change to Product, Market, City, Pricing Mode, Price, or Budget triggers a
recalculation across all models, metrics, decision cards, charts, and pages.
"""

import streamlit as st
from typing import Dict, Any, Optional
import sys
from pathlib import Path

ENGINE_PATH = Path(__file__).resolve().parents[2] / "MODEL" / "decision_engine"
if str(ENGINE_PATH) not in sys.path:
    sys.path.insert(0, str(ENGINE_PATH))

from decision_engine import decide_opportunity
from calculations import (
    load_product_catalog,
    get_recommended_price,
    compute_price_sensitivity,
    compute_budget_plan,
    compute_market_gaps
)

def init_global_state():
    """Initializes global state if not present."""
    if "app_state" not in st.session_state:
        st.session_state["app_state"] = {
            "lang": "en",
            "mode": "DYNAMIC",
            "dataset_key": "all_datasets",
            "product_id": "85123A",
            "market": "United States",
            "city": None,
            "pricing_mode": "auto",  # 'auto' or 'custom'
            "custom_price": None,
            "budget": 5000.0,
            "assumed_unit_cost": None,
            "active_screen": "DECIDE",
            "splash_dismissed": False
        }

def get_app_state() -> Dict[str, Any]:
    init_global_state()
    return st.session_state["app_state"]

def set_app_state_val(key: str, val: Any):
    """Updates a global state variable and invalidates computed cache."""
    init_global_state()
    if st.session_state["app_state"].get(key) != val:
        st.session_state["app_state"][key] = val
        invalidate_analysis()

def invalidate_analysis():
    """Forces cascade re-computation on next access."""
    if "analysis_cache" in st.session_state:
        del st.session_state["analysis_cache"]

def get_analysis_bundle() -> Dict[str, Any]:
    """
    Authoritative analysis pipeline.
    Produces ONE unified result consumed by ALL pages:
    Decide, Why, Pricing, Plan Entry, Market Gaps, Explore, and Static.
    """
    init_global_state()
    state = st.session_state["app_state"]
    
    # Check cache
    if "analysis_cache" in st.session_state:
        return st.session_state["analysis_cache"]

    product_id = state["product_id"]
    market = state["market"]
    city = state["city"]
    dataset_key = state["dataset_key"]
    budget = float(state["budget"])
    
    # 1. Price Recommendation
    price_rec = get_recommended_price(product_id, market, city=city, dataset_key=dataset_key)
    center_price = price_rec["price_center"]
    
    # 2. Determine Effective Selling Price
    if state["pricing_mode"] == "custom" and state.get("custom_price") and float(state["custom_price"]) > 0:
        effective_price = float(state["custom_price"])
    else:
        effective_price = center_price
        
    # 3. Decision Engine & Model Inference
    assumptions = {
        "budget": budget,
        "price": effective_price,
        "unit_cost": state.get("assumed_unit_cost")
    }
    decision_card = decide_opportunity(
        product_id=product_id,
        market=market,
        dataset_key=dataset_key,
        assumptions=assumptions,
        city=city
    )

    # 4. Price Sensitivity Curve
    price_sens = compute_price_sensitivity(
        product_id=product_id,
        market=market,
        dataset_key=dataset_key,
        selected_price=effective_price
    )

    # 5. Budget Plan & Break-Even Timeline
    budget_plan = compute_budget_plan(
        budget=budget,
        product_id=product_id,
        market=market,
        price=effective_price,
        dataset_key=dataset_key
    )

    # 6. Market Gaps
    market_gaps = compute_market_gaps()

    bundle = {
        "product_id": product_id,
        "market": market,
        "city": city,
        "dataset_key": dataset_key,
        "effective_price": effective_price,
        "budget": budget,
        "price_recommendation": price_rec,
        "decision": decision_card,
        "price_sensitivity": price_sens,
        "budget_plan": budget_plan,
        "market_gaps": market_gaps,
        "metrics": decision_card.get("metrics", {})
    }
    
    st.session_state["analysis_cache"] = bundle
    return bundle