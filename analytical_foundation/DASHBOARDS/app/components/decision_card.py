"""
DECISION CARD COMPONENT (Clean Flush-Left HTML, Zero Raw Code Leaks)
"""

import streamlit as st
from components.i18n import t, get_current_lang

def render_decision_card(res: dict):
    cur_lang = get_current_lang()
    decision = res.get("decision", "TEST")
    headline = res.get("headline", "")
    opp_score = res.get("opportunity_score", 0)
    success_prob = res.get("success_probability")
    indicators = res.get("indicators", {})
    checklist = res.get("action_checklist", [])
    metrics = res.get("metrics", {})
    price_rec = res.get("price_recommendation", {})
    model_name = metrics.get("model_used", "Calibrated Random Forest Classifier")
    
    color_map = {
        "ENTER": ("#065f46", "#f0fdf4", "#059669"),
        "TEST": ("#92400e", "#fffbeb", "#d97706"),
        "WATCH": ("#1e40af", "#eff6ff", "#2563eb"),
        "AVOID": ("#991b1b", "#fef2f2", "#dc2626"),
        "INSUFFICIENT_EVIDENCE": ("#475569", "#f8fafc", "#64748b")
    }
    text_c, bg_c, border_c = color_map.get(decision, ("#1e293b", "#f8fafc", "#64748b"))
    verdict_label = t(f"verdict_{decision}", cur_lang)
    
    # 1. PRIMARY CARD: Flush-left HTML without code-block indentations
    card_html = f"""<div style="background:{bg_c};border:1px solid {border_c};border-radius:8px;padding:12px 16px;margin-bottom:8px;">
<div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;">
<div style="display:flex;align-items:center;gap:12px;">
<span style="background:{border_c};color:#ffffff;padding:4px 14px;border-radius:4px;font-weight:800;font-size:1.15rem;letter-spacing:0.04em;">{verdict_label}</span>
<span style="font-size:1.6rem;font-weight:800;color:#0f172a;">{opp_score:.0f} <span style="font-size:0.95rem;color:#64748b;font-weight:600;">/ 100 {t('card_opportunity_score', cur_lang)}</span></span>
</div>
<div style="text-align:right;">
<div style="font-size:0.75rem;color:#64748b;font-weight:700;text-transform:uppercase;">{t('card_success_prob', cur_lang)}</div>
<div style="font-size:1.45rem;font-weight:800;color:{border_c};">{f"{success_prob:.0f}%" if success_prob is not None else "N/A"}</div>
</div>
</div>
<p style="font-size:0.98rem;font-weight:600;color:{text_c};margin-top:8px;margin-bottom:8px;line-height:1.4;">{headline}</p>
<div style="font-size:0.80rem;color:#475569;display:flex;flex-wrap:wrap;gap:14px;background:rgba(255,255,255,0.85);padding:6px 10px;border-radius:4px;border:1px solid #e2e8f0;">
<span>{t('card_product', cur_lang)}: <strong>{metrics.get('product_name', metrics.get('product_id', 'Item'))[:42]}</strong></span>
<span>{t('card_category', cur_lang)}: <strong>{metrics.get('category', 'General')}</strong></span>
<span>{t('card_rec_price', cur_lang)}: <strong>{price_rec.get('formatted_range', 'N/A')}</strong></span>
<span>{t('card_model_used', cur_lang)}: <strong>{model_name}</strong></span>
</div>
</div>"""
    st.markdown(card_html, unsafe_allow_html=True)
    
    # 2. SECONDARY CARDS: Indicators
    st.caption(t("card_indicators_title", cur_lang))
    cols = st.columns(5)
    with cols[0]:
        st.metric(t("ind_opportunity", cur_lang), f"{opp_score:.0f} / 100")
    with cols[1]:
        st.metric(t("ind_demand", cur_lang), indicators.get("demand", "Moderate"))
    with cols[2]:
        st.metric(t("ind_success", cur_lang), f"{success_prob:.0f}%" if success_prob is not None else "N/A")
    with cols[3]:
        st.metric(t("ind_economics", cur_lang), str(indicators.get("economics", "Neutral"))[:16])
    with cols[4]:
        st.metric(t("ind_risk", cur_lang), indicators.get("risk", "Low"))
        
    # 3. TERTIARY CARD: Action Checklist & Navigation
    st.markdown(f"**{t('card_actions_title', cur_lang)}**")
    act_c1, act_c2 = st.columns(2)
    for idx, item in enumerate(checklist[:4]):
        target_c = act_c1 if idx % 2 == 0 else act_c2
        with target_c:
            st.markdown(f"[+] {item}")

    st.markdown("---")
    
    btn_cols = st.columns(4)
    with btn_cols[0]:
        if st.button(t("btn_view_why", cur_lang), type="primary", use_container_width=True, key="card_btn_why"):
            st.session_state["app_state"]["active_screen"] = "WHY"
            st.rerun()
    with btn_cols[1]:
        if st.button(t("btn_view_pricing", cur_lang), type="secondary", use_container_width=True, key="card_btn_pricing"):
            st.session_state["app_state"]["active_screen"] = "PRICING"
            st.rerun()
    with btn_cols[2]:
        if st.button(t("btn_view_plan", cur_lang), type="secondary", use_container_width=True, key="card_btn_plan"):
            st.session_state["app_state"]["active_screen"] = "PLAN_ENTRY"
            st.rerun()
    with btn_cols[3]:
        if st.button(t("btn_view_markets", cur_lang), type="secondary", use_container_width=True, key="card_btn_markets"):
            st.session_state["app_state"]["active_screen"] = "MARKET_GAPS"
            st.rerun()