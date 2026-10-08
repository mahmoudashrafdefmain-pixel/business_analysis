"""
PAGE 6: WHAT-IF SIMULATOR SCREEN (Dynamically Tied to Active Product & Price)
"""

import streamlit as st
import plotly.graph_objects as go
import numpy as np
from components.i18n import t, get_current_lang
from components.state import get_analysis_bundle, set_app_state_val

def render_explore_screen():
    cur_lang = get_current_lang()
    bundle = get_analysis_bundle()
    effective_price = bundle["effective_price"]
    metrics = bundle["metrics"]
    base_units = int(metrics.get("units", 250))
    
    st.markdown(f"""<div style="font-size:1.25rem;font-weight:800;color:#0f172a;margin-bottom:2px;">
{t("explore_title", cur_lang)}
</div>
<div style="font-size:0.82rem;color:#64748b;margin-bottom:8px;">
{t("explore_sub", cur_lang)}
</div>""", unsafe_allow_html=True)

    # 1. PARAMETERS ROW
    c1, c2, c3 = st.columns(3)
    with c1:
        sim_price = st.number_input(
            "Selling Price ($)",
            value=float(effective_price),
            step=5.0,
            key="explore_sim_price"
        )
        if sim_price != effective_price:
            set_app_state_val("pricing_mode", "custom")
            set_app_state_val("custom_price", sim_price)
            st.rerun()
    with c2:
        sim_cost = st.number_input(
            "Assumed Unit Procurement Cost ($)",
            value=round(sim_price * 0.45, 2),
            step=2.0,
            key="explore_sim_cost"
        )
    with c3:
        sim_volume = st.number_input(
            "Monthly Volume (Units)",
            value=max(50, base_units),
            step=25,
            key="explore_sim_vol"
        )

    unit_margin = sim_price - sim_cost
    margin_pct = (unit_margin / max(0.01, sim_price)) * 100
    fixed_overhead = 1200.0
    monthly_net = (unit_margin * sim_volume) - fixed_overhead

    # 2. KPI METRICS
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.metric("Unit Margin", f"${unit_margin:.2f}")
    with k2:
        st.metric("Margin %", f"{margin_pct:.1f}%")
    with k3:
        st.metric("Gross Profit", f"${unit_margin * sim_volume:,.2f}")
    with k4:
        st.metric("Net Contribution", f"${monthly_net:,.2f}")

    # 3. TWO CHARTS SIDE BY SIDE (1 Chart = 1 Question)
    ch1, ch2 = st.columns(2)
    with ch1:
        st.caption(t('explore_chart1_title', cur_lang))
        costs = np.linspace(sim_cost * 0.5, sim_cost * 1.8, 12)
        margins = [(sim_price - c) / sim_price * 100 for c in costs]
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=costs, y=margins, mode="lines+markers", line=dict(color="#059669", width=2.5)))
        fig1.update_layout(height=230, margin=dict(l=30, r=20, t=10, b=25), template="plotly_white")
        st.plotly_chart(fig1, use_container_width=True)

    with ch2:
        st.caption(t('explore_chart2_title', cur_lang))
        vols = np.linspace(20, max(500, sim_volume * 2), 12)
        profits = [unit_margin * v - fixed_overhead for v in vols]
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=vols, y=profits, mode="lines+markers", line=dict(color="#2563eb", width=2.5)))
        fig2.add_hline(y=0, line_dash="dash", line_color="#dc2626")
        fig2.update_layout(height=230, margin=dict(l=30, r=20, t=10, b=25), template="plotly_white")
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")
    if st.button(t("btn_back_to_decide", cur_lang), type="primary", key="explore_back_btn"):
        set_app_state_val("active_screen", "DECIDE")
        st.rerun()