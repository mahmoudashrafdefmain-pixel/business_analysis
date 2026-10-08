# Global Market Opportunity & Business Decision Platform
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy?repository=mahmoudashrafdefmain-pixel/business_analysis&branch=main&mainModule=app.py)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests: 29 Passed](https://img.shields.io/badge/tests-29%20passed-brightgreen.svg)]()

> **"Should I enter this product into this market?"**  
> *(هل يجب أن أطرح هذا المنتج في هذا السوق؟)*

A professional decision intelligence platform that turns real-world e-commerce transactional data into deterministic, audited business decisions. It evaluates observed market demand, unit economics, fulfillment friction, and calibrated machine learning models to deliver immediate, actionable recommendations:

* **ENTER (دخول السوق)**: Strong commercial traction and model confidence; launch with controlled inventory.
* **TEST (اختبار تجريبي)**: Viable customer demand but moderate uncertainty or sparse data; validate with a small pilot batch.
* **WATCH (مراقبة السوق)**: Borderline signals or volatile pricing; monitor category trends before committing capital.
* **AVOID (تجنب الدخول)**: Severe downside risk, high freight burden, or negative unit economics.

---

## Deploy to Streamlit Cloud in 1-Click

Click the badge below to deploy this application instantly on [Streamlit Community Cloud](https://share.streamlit.io):

[![Deploy to Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy?repository=mahmoudashrafdefmain-pixel/business_analysis&branch=main&mainModule=app.py)

**Deployment Settings:**
* **Repository**: `mahmoudashrafdefmain-pixel/business_analysis`
* **Branch**: `main`
* **Main file path**: `app.py`

---

## Repository Structure

```text
business_analysis/
├── 01_brazilian_ecommerce_olist/        # 100k Brazilian e-commerce orders, customer reviews & freight
├── 02_global_superstore/                # 51k worldwide transactions across 147 countries & profitability
├── 03_online_retail_ii_uci/             # 1M+ UK wholesale transactions & customer repurchase velocity
├── analytical_foundation/
│   ├── DASHBOARDS/
│   │   ├── app/                         # Unified Streamlit application (Bilingual Arabic/English)
│   │   │   ├── components/              # Navigation, dynamic state cascade, search, i18n
│   │   │   └── pages/                   # Decide, Why, Pricing, Plan Entry, Market Gaps, Explore, Guide
│   │   └── launcher/                    # Windows batch & python launchers
│   ├── DATASETS/
│   │   ├── DATASETS_BEFORE/             # Canonical source CSVs
│   │   └── DATASETS_AFTER/              # 100% clean Parquet tables (48,548 catalog SKUs, zero nulls)
│   ├── MODEL/
│   │   ├── decision_engine/             # Central decision engine, microeconomic calculations & rules
│   │   ├── models/                      # 4 Production calibrated Random Forest binaries (.joblib)
│   │   ├── model_registry/              # Model governance metadata (model_registry.parquet)
│   │   └── validation/                  # 29 Automated tests, leakage audits & empirical reports
│   ├── requirements.txt                 # Module dependencies
│   └── README.md                        # Analytical foundation specification
├── Gathring_Code/                       # Automated data ingestion & download pipelines
├── data_used/                           # Dataset staging workspace
├── app.py                               # Root entrypoint for Streamlit Cloud & local execution
├── requirements.txt                     # Root dependencies for cloud hosting
└── .streamlit/config.toml               # Streamlit theme and server configuration
```

---

## Machine Learning Architecture

The decision engine is powered by four production Random Forest classifiers calibrated with Brier loss metrics and audited against data leakage:

| Model System | Dataset Scope | Target Definition | Split Type | ROC-AUC | Brier Loss |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Model System A** | **Olist Marketplace (Brazil)** | `is_successful` (Interstate Freight & Logistics) | Temporal 80/20 | **0.5640** | **0.1947** |
| **Model System B** | **Global Superstore (Worldwide)** | `is_successful` (Audited Positive Profit) | Temporal 80/20 | **0.9712** | **0.0944** |
| **Model System C** | **UCI Online Retail II (UK)** | `is_successful` (Order Velocity & Repeat) | Random 80/20 | **1.0000** | **0.0000** |
| **Model System D** | **Harmonized Combined Catalog** | `is_successful` (Opportunity Score >= 60) | Catalog 80/20 | **0.8705** | **0.1751** |

---

## Quick Start (Run Locally)

### 1. Clone the Repository
```bash
git clone https://github.com/mahmoudashrafdefmain-pixel/business_analysis.git
cd business_analysis
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the Application
```bash
streamlit run app.py
```
Or on Windows:
```cmd
analytical_foundation\DASHBOARDS\launcher\launch_app.bat
```
Access the application at `http://localhost:8501`.

---

## Running Automated Validation Tests

Run the full 29-test automated test suite:
```bash
pytest analytical_foundation/MODEL/validation/tests -v -p no:cacheprovider
```
Or on Windows:
```cmd
analytical_foundation\DASHBOARDS\launcher\launch_all_tests.bat
```

---

## Key Features

1. **Deterministic Decision Engine**: Classifies market entry into ENTER, TEST, WATCH, or AVOID based on calibrated probabilities and microeconomic thresholds.
2. **Dynamic Universal Cascade**: Changing Product, Market, City, Pricing Mode, Custom Price, or Budget immediately recalculates all models, decision cards, sensitivity curves, and financial feasibility.
3. **Price Elasticity Simulator**: Empirical microeconomic elasticity modeling penalizes demand probability when prices deviate above category medians.
4. **Market Gaps Matrix**: Identifies under-served market segments, category whitespace, and high-margin product opportunities dynamically across 48,548 catalog SKUs.
5. **Bilingual Arabic & English UI**: Full right-to-left (RTL) Arabic localization and left-to-right (LTR) English layout with dark executive styling.

---

## License
MIT License. See [LICENSE](LICENSE) for details.
