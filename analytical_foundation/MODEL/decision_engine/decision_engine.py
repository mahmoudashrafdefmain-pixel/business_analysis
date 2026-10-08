"""
CENTRAL DECISION ENGINE (Production Version - Sections 86-132)
Produces ONE authoritative decision card for:
"Should I enter this product into this market?"
Decisions: ENTER | TEST | WATCH | AVOID | INSUFFICIENT_EVIDENCE
Features:
- Calibrated Random Forest inference (Olist, GS, UCI, Combined)
- Complete WHY Narrative (What Supports [✓], What Hurts [⚠], Final Reason)
- City & Market-Level Price Intelligence & Sensitivity
- Budget Feasibility & Break-Even Timeline
"""

from typing import Dict, Any, Optional
from decision_rules import DECISION_THRESHOLDS
from calculations import (
    compute_product_metrics, 
    get_recommended_price, 
    compute_price_sensitivity, 
    compute_budget_plan
)

def decide_opportunity(
    product_id: str,
    market: str,
    dataset_key: str = "all_datasets",
    assumptions: Optional[Dict[str, Any]] = None,
    city: Optional[str] = None
) -> Dict[str, Any]:
    """
    Evaluates product market entry and returns single comprehensive decision card.
    """
    metrics = compute_product_metrics(product_id, market, dataset_key, assumptions)
    if not metrics:
        return {
            "decision": "INSUFFICIENT_EVIDENCE",
            "headline": "Product not found in registry.",
            "opportunity_score": 0,
            "success_probability": None,
            "confidence": "Insufficient",
            "indicators": {
                "opportunity": "0 / 100",
                "demand": "Unknown",
                "success_prob": "N/A",
                "economics": "Unknown",
                "risk": "High"
            },
            "evidence_blocks": [],
            "action_checklist": ["Select a valid catalog product from the list."],
            "how_calculated": {
                "data_used": "None",
                "model": "None",
                "limitations": "Product not found in reconciled catalog"
            },
            "why_breakdown": {
                "supports": [],
                "hurts": ["⚠ Product SKU not matched in audited database"],
                "final_reason": "No historical transaction or catalog record exists for this product ID."
            },
            "price_recommendation": None,
            "price_sensitivity": None,
            "budget_plan": None,
            "metrics": {}
        }

    # Fetch price recommendation and price sensitivity
    price_rec = get_recommended_price(product_id, market, city=city, dataset_key=dataset_key)
    selected_price = assumptions.get("price") if assumptions else None
    price_sens = compute_price_sensitivity(product_id, market, dataset_key=dataset_key, selected_price=selected_price)
    
    # Budget planning
    user_budget = float(assumptions.get("budget", 5000.0)) if assumptions and "budget" in assumptions else 5000.0
    budget_plan = compute_budget_plan(user_budget, product_id, market, price=selected_price, dataset_key=dataset_key)

    # 1. Cold Start Check
    if metrics["is_cold_start"]:
        rule = DECISION_THRESHOLDS["INSUFFICIENT_EVIDENCE"]
        return {
            "decision": "TEST",
            "headline": rule["headline"],
            "opportunity_score": metrics["opportunity_score"],
            "success_probability": None,
            "confidence": "Insufficient",
            "indicators": {
                "opportunity": f"{metrics['opportunity_score']:.0f} / 100",
                "demand": "Weak / Sparse",
                "success_prob": "Insufficient Data",
                "economics": metrics["economic_rating"],
                "risk": "Moderate (Data Uncertainty)"
            },
            "evidence_blocks": [
                {
                    "title": "Historical Evidence",
                    "status": "Sparse",
                    "summary": f"Only {metrics['orders']} orders recorded historically. Statistical confidence requires at least 5 observations.",
                    "importance": "High"
                },
                {
                    "title": "Recommended Posture",
                    "status": "Pilot Only",
                    "summary": "Do not commit significant inventory until sell-through is empirically validated.",
                    "importance": "High"
                }
            ],
            "action_checklist": rule["checklist"],
            "how_calculated": {
                "data_used": f"{metrics['dataset_key'].upper()} line transactions",
                "model": "Cold-Start Rule (orders < 5)",
                "limitations": "No historical volume baseline; pilot test required"
            },
            "why_breakdown": {
                "supports": [
                    f"✓ Product belongs to active category: {metrics['category']}",
                    f"✓ Entry price point {price_rec['formatted_range']} is accessible"
                ],
                "hurts": [
                    f"⚠ Historical volume is sparse ({metrics['orders']} orders)",
                    "⚠ Statistical confidence is insufficient for full capital commitment"
                ],
                "final_reason": f"With only {metrics['orders']} historical transactions, full-scale commercial commitment carries high uncertainty. A controlled pilot test of {budget_plan['purchasable_units']} units is advised before expanding."
            },
            "price_recommendation": price_rec,
            "price_sensitivity": price_sens,
            "budget_plan": budget_plan,
            "metrics": metrics
        }

    # 2. Decision Thresholds & Score Evaluation
    opp = metrics["opportunity_score"]
    prob = metrics["success_probability"] or 50.0
    risk = metrics["risk_rating"]
    econ = metrics["economic_rating"]

    if opp >= 75 and prob >= 65 and risk != "High":
        decision = "ENTER"
    elif opp >= 55 and prob >= 48 and risk != "High":
        decision = "TEST"
    elif opp >= 40:
        decision = "WATCH"
    else:
        decision = "AVOID"

    rule = DECISION_THRESHOLDS[decision]

    # Evidence Blocks (4 to 6 concise blocks)
    evidence = [
        {
            "title": "Market Demand",
            "status": metrics["demand_rating"],
            "summary": f"Observed volume ({metrics['orders']} orders, {metrics['units']} units) demonstrates {metrics['demand_rating'].lower()} buyer traction in {market}.",
            "importance": "High"
        },
        {
            "title": "Commercial Traction",
            "status": f"{prob:.0f}% Likelihood",
            "summary": f"{metrics.get('model_used', 'Calibrated Random Forest')} estimates a {prob:.0f}% probability of sustainable top-tier performance.",
            "importance": "High"
        },
        {
            "title": "Unit Economics",
            "status": econ,
            "summary": f"Target price is {price_rec['formatted_range']}. " + (
                f"Audited profit margin is {metrics['native_profit']:.2f} {metrics['currency_code']}." if metrics['has_native_profit']
                else "Procurement cost not in source data; simulated via unit cost assumption."
            ),
            "importance": "Medium"
        },
        {
            "title": "Pricing & Capital",
            "status": "Feasible" if budget_plan["is_feasible"] else "Capital Constrained",
            "summary": f"Budget of {price_rec['currency_symbol']}{user_budget:,.0f} supports {budget_plan['purchasable_units']} units. Est. break-even timeline: {budget_plan['break_even_timeline']}.",
            "importance": "Medium"
        },
        {
            "title": "Downside Risk",
            "status": risk,
            "summary": f"Risk profile is categorized as {risk.lower()} based on category volatility, fulfillment requirements, and price elasticity.",
            "importance": "Medium"
        }
    ]

    # 3. Complete WHY Breakdown
    supports = []
    hurts = []

    if opp >= 60:
        supports.append(f"✓ Strong Market Opportunity: Score of {opp:.0f}/100 exceeds baseline threshold")
    if prob >= 55:
        supports.append(f"✓ Model Confidence: {metrics.get('model_used', 'Calibrated RF')} projects {prob:.0f}% success probability")
    if metrics["orders"] >= 15:
        supports.append(f"✓ Proven Demand Velocity: {metrics['orders']} orders and {metrics['units']} units recorded historically")
    if budget_plan["is_feasible"]:
        supports.append(f"✓ Capital Feasibility: Available budget exceeds minimum pilot threshold ({price_rec['currency_symbol']}{budget_plan['min_capital_required']:,.0f})")
    if metrics["has_native_profit"] and metrics["native_profit"] > 0:
        supports.append(f"✓ Verified Profitability: Native margin is positive ({metrics['currency_symbol']}{metrics['native_profit']:.2f})")
    elif len(supports) < 2:
        supports.append(f"✓ Accessible Product Category: Active demand in {metrics['category']}")

    if risk == "High":
        hurts.append("⚠ Elevated Downside Risk: High concentration or volatile demand patterns")
    if not budget_plan["is_feasible"]:
        hurts.append(f"⚠ Capital Constraint: Current budget is below minimum recommended pilot capital ({price_rec['currency_symbol']}{budget_plan['min_capital_required']:,.0f})")
    if prob < 50:
        hurts.append(f"⚠ Sub-50% Success Likelihood: Random Forest projects only {prob:.0f}% success probability")
    if metrics["orders"] < 10:
        hurts.append(f"⚠ Low Order Velocity: Only {metrics['orders']} transactions recorded")
    if opp < 50:
        hurts.append(f"⚠ Low Category Opportunity: Market opportunity score is below benchmark ({opp:.0f}/100)")
    if len(hurts) == 0:
        hurts.append("⚠ Fulfillment and supply chain execution must be monitored during initial rollout")

    # Synthesized Final Reason paragraph
    if decision == "ENTER":
        final_reason = (
            f"Audited market data and the {metrics.get('model_used', 'Calibrated Random Forest')} indicate robust commercial traction "
            f"for '{metrics['product_name']}' in {market}. With an opportunity score of {opp:.0f}/100, an estimated success probability of {prob:.0f}%, "
            f"and sound unit economics at {price_rec['formatted_range']}, empirical conditions strongly support immediate market entry."
        )
    elif decision == "TEST":
        final_reason = (
            f"Transactional evidence demonstrates viable buyer demand ({metrics['orders']} orders) in {market}, but requires controlled execution. "
            f"With a {prob:.0f}% model success probability and moderate risk factors, an initial pilot of approximately {budget_plan['purchasable_units']} "
            f"units is recommended to validate sell-through prior to full capital deployment."
        )
    elif decision == "WATCH":
        final_reason = (
            f"Current indicators for '{metrics['product_name']}' in {market} show borderline viability (Opportunity: {opp:.0f}/100, Success: {prob:.0f}%). "
            f"Demand velocity or margin cushions are insufficient to justify immediate inventory expenditure. Recommend monitoring competitive shifts."
        )
    else: # AVOID
        final_reason = (
            f"Empirical analysis reveals unfavorable risk-reward dynamics (Opportunity: {opp:.0f}/100, Success: {prob:.0f}%). "
            f"High fulfillment friction, soft transaction velocity, or negative economics make market entry unviable under current parameters."
        )

    return {
        "decision": decision,
        "headline": rule["headline"],
        "opportunity_score": opp,
        "success_probability": prob,
        "confidence": metrics["confidence"],
        "indicators": {
            "opportunity": f"{opp:.0f} / 100",
            "demand": metrics["demand_rating"],
            "success_prob": f"{prob:.0f}%",
            "economics": econ,
            "risk": risk
        },
        "evidence_blocks": evidence,
        "action_checklist": rule["checklist"],
        "how_calculated": {
            "data_used": f"Historical {metrics['dataset_key'].replace('_', ' ').title()} transactions",
            "model": metrics.get("model_used", "Calibrated Random Forest Classifier"),
            "limitations": "Reflects observed sales; does not account for sudden macroeconomic shifts"
        },
        "why_breakdown": {
            "supports": supports,
            "hurts": hurts,
            "final_reason": final_reason
        },
        "price_recommendation": price_rec,
        "price_sensitivity": price_sens,
        "budget_plan": budget_plan,
        "metrics": metrics
    }
