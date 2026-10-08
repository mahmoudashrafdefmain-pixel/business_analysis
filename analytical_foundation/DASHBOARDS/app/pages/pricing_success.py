"""
PAGE 3: PRICING SCREEN (Flush-Left HTML, State-Synchronized)
"""

import streamlit as st
import plotly.graph_objects as go
from components.i18n import t, get_current_lang
from components.state import get_analysis_bundle, set_app_state_val

def render_pricing_screen():
    cur_lang = get_current_lang()
    bundle = get_analysis_bundle()
    price_info = bundle["price_recommendation"]
    sens = bundle["price_sensitivity"]
    center = price_info["price_center"]
    sym = price_info["currency_symbol"]
    effective_price = bundle["effective_price"]
    
    st.markdown(f"""<div style="font-size:1.25rem;font-weight:800;color:#0f172a;margin-bottom:2px;">
{t("pricing_title", cur_lang)}
</div>
<div style="font-size:0.82rem;color:#64748b;margin-bottom:8px;">
{t("pricing_sub", cur_lang)}
</div>""", unsafe_allow_html=True)

    # 1. PRIMARY CARD: Price KPI Panels
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(t("pricing_rec_range", cur_lang), price_info["formatted_range"])
    with c2:
        st.metric(t("pricing_optimal", cur_lang), f"{sym}{center:.2f}")
    with c3:
        st.metric(t("pricing_scope", cur_lang), price_info["evidence_level"])

    # 2. SECONDARY CARD: Interactive Slider & Elasticity Feedback
    min_slider = round(center * 0.60, 2)
    max_slider = round(center * 1.50, 2)
    
    selected_price = st.slider(
        f"{t('pricing_slider_label', cur_lang)} ({sym})",
        min_value=min_slider,
        max_value=max_slider,
        value=min(max(effective_price, min_slider), max_slider),
        step=max(0.5, round((max_slider - min_slider) / 40, 2)),
        key="pricing_slider_comp"
    )
    if selected_price != effective_price:
        set_app_state_val("pricing_mode", "custom")
        set_app_state_val("custom_price", selected_price)
        st.rerun()

    cur_prob = sens["selected_success_probability"]
    curve_points = sens["curve_points"]

    # 3. TERTIARY CARD: Compact Sensitivity Plotly Chart
    x_prices = [p["price"] for p in curve_points]
    y_probs = [p["success_probability"] for p in curve_points]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x_prices, y=y_probs,
        mode="lines+markers",
        name="Sensitivity Curve",
        line=dict(color="#2563eb", width=2.5),
        marker=dict(size=7, color="#1e40af")
    ))
    fig.add_trace(go.Scatter(
        x=[selected_price], y=[cur_prob],
        mode="markers",
        name="Target Price",
        marker=dict(size=12, color="#dc2626")
    ))
    fig.add_vrect(
        x0=price_info["price_low"], x1=price_info["price_high"],
        fillcolor="rgba(5, 150, 105, 0.12)",
        layer="below", line_width=0,
        annotation_text="Optimal Corridor",
        annotation_position="top left"
    )
    fig.update_layout(
        xaxis_title=f"Price ({sym})",
        yaxis_title="Success Prob (%)",
        yaxis=dict(range=[15, 100]),
        margin=dict(l=35, r=35, t=25, b=30),
        height=270,
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Action Buttons Row
    b1, b2 = st.columns([1.5, 4])
    with b1:
        if st.button(t("btn_apply_price", cur_lang), type="primary", use_container_width=True, key="apply_price_btn"):
            set_app_state_val("active_screen", "DECIDE")
            st.rerun()
    with b2:
        if st.button(t("btn_back_to_decide", cur_lang), type="secondary", key="pricing_back_btn"):
            set_app_state_val("active_screen", "DECIDE")
            st.rerun()