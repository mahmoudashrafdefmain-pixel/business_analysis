# Product Market Entry Decision Platform

A professional decision intelligence platform designed around one core business decision:

> **"Should I enter this product into this market?"**  
> *(هل يجب أن أطرح هذا المنتج في هذا السوق؟)*

The platform evaluates observed market demand, unit economics, fulfillment friction, and calibrated machine learning models to deliver an immediate, deterministic recommendation:

* **ENTER (دخول السوق)**: Strong commercial traction and model confidence; launch with controlled pilot inventory.
* **TEST (اختبار تجريبي)**: Viable customer demand but moderate uncertainty or sparse data; validate with small pilot batch.
* **WATCH (مراقبة السوق)**: Borderline signals or volatile pricing; monitor category trends before committing inventory capital.
* **AVOID (تجنب الدخول)**: Severe downside risk, high freight burden, or negative unit economics.

---

## Key Interface & Architectural Features (Sections 176–222)

1. **Dark Professional Splash Screen**: Pitch black (`#050505`), pure white (`#ffffff`), and crimson red (`#dc2626`) palette featuring the 4-word title `GLOBAL MARKET DECISION INTELLIGENCE` and a pulsing central geometric SVG nexus emblem with instant entry and discreet intro replay.
2. **Single Source of Truth (`AppState`) Universal Cascade**: Changing any input parameter (`dataset_scope`, `product`, `market`, `city`, `pricing_mode`, `custom_price`, `budget`) instantly cascades through data filtering, feature vectors, dedicated Random Forest models, decision engine, sensitivity curves, and all pages.
3. **Pure Dynamic Analytics & Zero Hardcoding**: Market gaps, category benchmark corridors, and price sensitivity points are dynamically derived from `product_market_reconciled.parquet` (48,548 catalog SKUs across Olist, Global Superstore, and UCI) and empirical response curves.
4. **Microeconomic Price Elasticity Multiplier**: Realistic demand elasticity scaling adjusts model success probability downwards when prices deviate significantly above category medians.
5. **Dedicated Pricing Mode Control**: Clean toggle between `Automatic recommended price` and `Enter custom target price` eliminating ambiguous zero-inputs.
6. **Zero Raw HTML Leakage & Duplicate Headings**: Completely unindented multiline HTML strings preventing markdown preformatted code blocks across all views.
7. **Complete Sidebar Removal & No-Scroll Card Architecture**: Pure top-level navigation bar with viewport-fitted Primary, Secondary, and Tertiary card panels.
8. **First-Class Arabic (`العربية`) & English Support**: Complete bilingual interface with natural business Arabic translations and automatic RTL/LTR layout transitions.
9. **Four Calibrated Production Random Forest Models**: Dedicated classifiers for Olist, Global Superstore, UCI Online Retail, and Harmonized Combined catalog.

---

## Quick Start & Launchers

Launch scripts are located in `DASHBOARDS/launcher/`:

| Launcher Script | Description |
| :--- | :--- |
| **`launch_app.bat`** (or `.py`) | Launches the primary unified web application on `http://localhost:8501` |
| **`launch_static.bat`** (or `.py`) | Launches directly into **Static Mode** (precomputed executive market overview) |
| **`launch_dynamic.bat`** (or `.py`) | Launches directly into **Dynamic Mode** (personalized interactive analysis) |
| **`launch_rf_models.bat`** (or `.py`) | Runs benchmark evaluation across all 4 production Random Forest models |
| **`launch_all_tests.bat`** | Runs the full 29-test automated validation suite |

To start immediately:
```cmd
DASHBOARDS\launcher\launch_app.bat
```

---

## Machine Learning Architecture (Four Random Forest Systems)

| Model System | Dataset Scope | Target Definition | Split Type | ROC-AUC | Brier Loss |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Model System A** | **Olist Marketplace (Brazil)** | `is_successful` (Interstate Freight & Logistics) | Temporal 80/20 | **0.5640** | **0.1947** |
| **Model System B** | **Global Superstore (Worldwide)** | `is_successful` (Audited Positive Profit) | Temporal 80/20 | **0.9712** | **0.0944** |
| **Model System C** | **UCI Online Retail II (UK)** | `is_successful` (Order Velocity & Wholesale Repeat) | Random 80/20 | **1.0000** | **0.0000** |
| **Model System D** | **Harmonized Combined Catalog** | `is_successful` (Opportunity Score >= 60) | Catalog 80/20 | **0.8705** | **0.1751** |

---

## Strict 3-Folder Structure

```text
analytical_foundation/
├── DATASETS/
│   ├── DATASETS_BEFORE/         # Canonical source CSVs
│   └── DATASETS_AFTER/          # 100% clean Parquet tables (48,548 catalog SKUs, zero nulls)
├── MODEL/
│   ├── models/                  # Calibrated RF model binaries (.joblib)
│   ├── model_registry/          # Model governance metadata (model_registry.parquet)
│   ├── validation/              # 29 Automated tests, leakage audits & input dependency reports
│   └── decision_engine/         # Central decision engine, smart search, and calculations
├── DASHBOARDS/
│   ├── launcher/                # Batch and Python launchers for apps and models
│   └── app/                     # Unified Streamlit application
│       ├── components/          # i18n localization, navigation, state engine, splash screen
│       ├── pages/               # Decide, Why, Pricing, Plan Entry, Market Gaps, Explore, Static, Guide
│       └── main.py              # Application entrypoint with zero dead buttons
├── README.md
├── requirements.txt
└── GUIDE.md
```
