"""
ONE METRIC DEFINITIONS REGISTRY (Section 42)
Central definitions for every key metric.
"""

METRIC_REGISTRY = {
    "opportunity_score": {
        "name": "Opportunity Score",
        "definition": "Composite 0-100 score measuring market demand, velocity, customer interest, and commercial traction.",
        "formula": "40% Demand Percentile + 25% Relative Price Health + 20% Customer Repeat + 15% Economics/Stability",
        "source": "Cleaned Transaction Ledgers",
        "unit": "Score (0-100)",
        "currency": "None (Normalized Index)",
        "grain": "Product x Market",
        "availability": "Universal across all 3 datasets"
    },
    "success_probability": {
        "name": "Success Probability",
        "definition": "Calibrated model-estimated likelihood that product achieves top-quartile velocity and healthy unit economics.",
        "formula": "LightGBM Classifier with Out-of-Domain Calibration (Evaluated via Brier Score)",
        "source": "Cross-Dataset Model System",
        "unit": "Percentage (%)",
        "currency": "None",
        "grain": "Product Observation",
        "availability": "Available when historical observations >= 5"
    },
    "demand_strength": {
        "name": "Demand Strength",
        "definition": "Relative volume of historical orders and units compared with market and category averages.",
        "formula": "High if volume percentile >= 70th; Moderate if 40th-69th; Weak if < 40th",
        "source": "Historical Order Items",
        "unit": "Rating (Strong / Moderate / Weak)",
        "currency": "None",
        "grain": "Market Level",
        "availability": "Universal across all 3 datasets"
    },
    "economic_health": {
        "name": "Economic Health",
        "definition": "Assessment of contribution margins and profitability safety margins.",
        "formula": "Global Superstore: Audited Operating Margin. Olist/UCI: Marked Not Available unless user assumption supplied.",
        "source": "Audited ERP for GS; User Assumptions for others",
        "unit": "Status (Healthy / Neutral / Dilutive / Not Available)",
        "currency": "Native (USD for GS, BRL for Olist, GBP for UCI)",
        "grain": "Product Line",
        "availability": "GS native; Olist/UCI via user assumption"
    },
    "risk_score": {
        "name": "Risk Level",
        "definition": "Assessment of commercial and operational downside (loss probability, delivery friction, discount vulnerability).",
        "formula": "Combined assessment of shipping delay risk, return/detractor risk, and discount cliff exposure (>20% cliff)",
        "source": "Operational Delay & Loss Classifiers",
        "unit": "Rating (Low / Moderate / High)",
        "currency": "None",
        "grain": "Market Level",
        "availability": "Universal across all 3 datasets"
    }
}
