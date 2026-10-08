# Global Input Dependency Audit & Data Flow Report

**Date**: October 8, 2026  
**Standards**: Sections 176–222 (End-to-End Dependency Pipeline, Zero Hardcoding, Single AppState)

---

## 1. Executive Summary

This audit verifies that every user input in the application strictly controls the analytical pipeline and that no output relies on hardcoded placeholders or decoupled local states.

```text
USER INPUT
    ↓
GLOBAL APPLICATION STATE (AppState)
    ↓
DATA FILTERING & LOOKUP (product_market_reconciled.parquet)
    ↓
FEATURE VECTOR GENERATION (Effective Price, Freight Ratio, Units, Velocity)
    ↓
MODEL SELECTION (Olist RF / GS RF / UCI RF / Harmonized Combined RF)
    ↓
CALIBRATED PROBABILITY INFERENCE
    ↓
CENTRAL DECISION ENGINE (decide_opportunity)
    ↓
PRICE SENSITIVITY & BUDGET FEASIBILITY
    ↓
UNIFIED OUTPUT BUNDLE (Single Source of Truth)
    ↓
ALL PAGES & VISUALIZATIONS (Decide, Why, Pricing, Plan Entry, Market Gaps, Explore, Static)
```

---

## 2. Input Dependency Matrix

| Input Variable | Where Created | Stored In | Consumed By | Mathematical Impact | Real Output Impact |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`dataset_key`** | Decide Screen Scope Selector | `AppState["dataset_key"]` | `load_clean_dataset`, `load_rf_model`, `search_products` | Activates dedicated RF model, currency ledger, and native feature vector | Controls model identity, BRL/USD/GBP currency, and product pool |
| **`product_id`** | Smart Search Bar / Dropdown | `AppState["product_id"]` | `compute_product_metrics`, `get_recommended_price` | Retrieves historical order volume, units, native price, and opportunity score | Directly drives Opportunity Score, Demand rating, and Model feature vector |
| **`market`** | Target Market Dropdown | `AppState["market"]` | `get_recommended_price`, `compute_product_metrics` | Applies geographic multiplier, sets interstate/cross-border freight flags | Shifts Recommended Price corridor, model success probability, and WHY risks |
| **`city`** | Target City Dropdown | `AppState["city"]` | `get_recommended_price` | Applies metropolitan purchasing-power multiplier (e.g. NYC 1.12, London 1.15) | Sets city-level price corridor and alters break-even capital requirement |
| **`pricing_mode`** | Pricing Mode Radio (`auto` vs `custom`) | `AppState["pricing_mode"]` | `get_analysis_bundle` | Toggles between empirical baseline price and user's specific price | Determines whether custom price overrides default in model features |
| **`custom_price`** | Custom Price Numeric Input | `AppState["custom_price"]` | Feature Engineering, `compute_price_sensitivity` | Injects price into RF features (`norm_price`, `freight_burden_ratio`, `Sales`) | Directly changes Model Success Probability, Unit Margin, and Break-Even |
| **`budget`** | Capital Budget Numeric Input | `AppState["budget"]` | `compute_budget_plan` | Compared against `min_capital_required` (100 units * unit cost * 1.25 buffer) | Controls Feasibility status (`Feasible` vs `Underfunded`), units, and timeline |
| **`lang`** | Top Language Switcher (`EN` / `AR`) | `AppState["lang"]` | `t(key, lang)`, `inject_layout_css` | Toggles dictionary and injects RTL (`direction: rtl`) or LTR | Flips layout, modern typography, currency labels, and all card texts |
| **`mode`** | Top Mode Switcher (`STATIC` / `DYNAMIC`) | `AppState["mode"]` | `main.py` routing | Toggles between precomputed market overview and user scenario evaluation | Controls page rendering without losing user state |

---

## 3. Hardcoded Value Purge Verification

1. **Market Matrix**: Formerly static dictionaries in `compute_market_gaps` have been connected to empirical catalog aggregations from `product_market_reconciled.parquet`.
2. **Price Sensitivity**: Generates 7 evaluation points directly scored by the calibrated Random Forest classifier.
3. **Budget Feasibility**: Evaluated directly against the active unit price and inventory batch requirement.
4. **Raw HTML Leakage**: Cleaned all leading indentations from `st.markdown` calls; eliminated code-block rendering bugs across Decide, Why, Pricing, and Guide.
5. **No Duplicate Titles**: Cleaned Guide topic display to eliminate repeated section headings.