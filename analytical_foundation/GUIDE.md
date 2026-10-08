# User & Developer Guide

---

# PART 1: USER GUIDE

## 1. Starting the Platform
Double-click `DASHBOARDS\launcher\launch_app.bat` or run:
```bash
python DASHBOARDS/launcher/launch_app.py
```
Open your browser at `http://localhost:8501`.

## 2. Splash Screen & Intro Experience
When first loading the platform, a dark-themed splash screen (`GLOBAL MARKET DECISION INTELLIGENCE`) appears with an animated crimson nexus emblem. Click **[ ENTER PLATFORM ]** to immediately access the decision interface. You can replay the intro anytime using the **[ Intro ]** button in the header.

## 3. Language Selection (English | العربية)
At the top right of the application header:
* Click **English** for English (LTR) layout.
* Click **العربية** for professional Arabic (RTL) layout.
* Language switching preserves all current selections, active product, market, price, budget, and active screen without resetting.

## 4. Pure Top-Level Navigation (Zero Sidebars)
The platform uses exclusively top-level controls:
* **Mode Switcher**: Toggle between **Static** (precomputed market benchmarks) and **Dynamic** (personalized interactive evaluation).
* **Screens**:
  * **Decide (القرار)**: Main decision portal with Scope, Smart Search, Market/City selectors, and Decision Card.
  * **Why? (المبررات)**: Breakdown of supporting factors (`[+]`), risk factors (`[!]`), and synthesized final reason.
  * **Price & Success (السعر والنجاح)**: Recommended price band, pricing mode toggle, and interactive 7-point sensitivity curve.
  * **Plan My Entry (خطة الدخول)**: Capital budget feasibility, batch inventory units, and break-even runway timeline.
  * **Market Gaps (فجوات السوق)**: Empirical cross-market diagnostic detailing products needed and lower-opportunity segments.
  * **What-If (المحاكاة)**: Unit margin and sales volume profit simulator (1 Chart = 1 Question).
  * **Guide (الدليل)**: Comprehensive interactive card-based guide explaining all platform functions.

## 5. No-Scroll Card Layout
Information is organized into compact panels:
* **Primary Card**: Verdict badge (`ENTER`, `TEST`, `WATCH`, `AVOID`), Opportunity Score (0–100), Success Probability (%), and Headline.
* **Secondary Cards**: Recommended Price, Risk Posture, and 5 Core Indicators.
* **Tertiary Cards**: Action Checklist and Next Steps.

---

# PART 2: DEVELOPER & AUDIT GUIDE

## 1. Single Source of Truth & Cascade (`components/state.py`)
All global inputs (`dataset_scope`, `product`, `market`, `city`, `pricing_mode`, `custom_price`, `budget`) are held in `AppState`. Modifying any input invalidates the analysis cache and cascades changes through data slicing, feature extraction, dedicated Random Forest inference, decision logic, sensitivity curves, and all downstream pages.

## 2. Interactive Guide System (`pages/guide.py`)
The Guide is rendered as modular cards with a topic selector covering:
1. Core Decision Focus
2. Static vs Dynamic Modes
3. Smart Product Search
4. Selecting Market & City
5. Recommended Price & Sensitivity Slider
6. Success Probability: Estimate vs Guarantee
7. Verdict Definitions (ENTER, TEST, WATCH, AVOID)
8. Understanding WHY
9. Market Gaps & Opportunities
10. Plan My Entry (Budget Feasibility)
11. Break-Even Profitability Timeline
12. Statistical Confidence & Cold-Start Protection
13. Data Hierarchy: Observed Fact vs Model Estimate vs User Assumption
14. Analytical Limitations & Governance
15. 4-Step Quick-Start Workflow

## 3. Running Automated Validation Tests
Run the 29-test automated validation suite:
```cmd
DASHBOARDS\launcher\launch_all_tests.bat
```
Or via Python:
```bash
python -m pytest MODEL/validation/tests -v
```
All 29 tests verify data integrity, currency preservation, absence of synthetic fallbacks, feature leakage prevention, probability calibration, decision engine logic, and global input cascade dependencies.
