"""
DECISION RULES & THRESHOLDS (Section 12)
Configurable decision criteria for: ENTER, TEST, WATCH, AVOID.
"""

DECISION_THRESHOLDS = {
    "ENTER": {
        "min_opportunity_score": 75,
        "min_success_prob": 0.65,
        "max_risk_score": 0.35,
        "headline": "Strong commercial opportunity in this market.",
        "recommended_action": "Launch with a controlled initial inventory.",
        "checklist": [
            "Review baseline demand in target geography",
            "Set launch price aligned with category median",
            "Confirm logistics lead times and buffer",
            "Start with limited pilot inventory to validate sell-through"
        ]
    },
    "TEST": {
        "min_opportunity_score": 55,
        "min_success_prob": 0.48,
        "max_risk_score": 0.55,
        "headline": "Potential opportunity; market validation advised.",
        "recommended_action": "Run a small pilot before committing full inventory.",
        "checklist": [
            "Test demand with small sample SKU batch",
            "Monitor conversion velocity against category benchmark",
            "Evaluate initial delivery satisfaction",
            "Scale inventory only after proven sell-through"
        ]
    },
    "WATCH": {
        "min_opportunity_score": 40,
        "min_success_prob": 0.35,
        "max_risk_score": 0.70,
        "headline": "Opportunity is uncertain or signals are volatile.",
        "recommended_action": "Monitor demand and competitive dynamics before entering.",
        "checklist": [
            "Track category growth trends over the next quarter",
            "Observe competitor pricing and discount moves",
            "Avoid capital commitment until volume stabilizes",
            "Re-assess when additional transaction evidence emerges"
        ]
    },
    "AVOID": {
        "headline": "Market fundamentals are currently unfavorable.",
        "recommended_action": "Do not allocate significant capital; explore alternatives.",
        "checklist": [
            "Redirect budget to higher-demand categories",
            "Investigate alternative markets with lower friction",
            "Avoid aggressive discounting which accelerates value loss",
            "Re-evaluate unit economics before considering re-entry"
        ]
    },
    "INSUFFICIENT_EVIDENCE": {
        "headline": "Insufficient historical observations for reliable recommendation.",
        "recommended_action": "Run a small exploratory test to gather initial baseline evidence.",
        "checklist": [
            "Catalog observations are too sparse for statistical confidence",
            "Do not commit significant capital without initial data",
            "Conduct micro-pilot to test consumer response",
            "Re-run analysis once transaction history is established"
        ]
    }
}
