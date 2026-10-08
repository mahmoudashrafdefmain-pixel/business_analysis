"""
PAGE 4: PLAN MY ENTRY SCREEN (Flush-Left HTML, State-Synchronized)
"""

import streamlit as st
from components.i18n import t, get_current_lang
from components.state import get_analysis_bundle, set_app_state_val

def render_plan_entry_screen():
    cur_lang = get_current_lang()
    bundle = get_analysis_bundle()
    plan = bundle["budget_plan"]
    sym = plan["currency_symbol"]
    is_feas = plan["is_feasible"]
    user_budget = bundle["budget"]
    
    st.markdown(f"""<div style="font-size:1.25rem;font-weight:800;color:#0f172a;margin-bottom:2px;">
{t("plan_title", cur_lang)}
</div>
<div style="font-size:0.82rem;color:#64748b;margin-bottom:8px;">
{t("plan_sub", cur_lang)}
</div>""", unsafe_allow_html=True)

    new_b = st.number_input(
        t("budget_label", cur_lang),
        min_value=100.0,
        max_value=1000000.0,
        value=user_budget,
        step=1000.0,
        key="budget_entry_input"
    )
    if new_b != user_budget:
        set_app_state_val("budget", new_b)
        st.rerun()

    # 1. PRIMARY STATUS BANNER (Flush-left)
    if is_feas:
        st.markdown(f"""<div style="background:#f0fdf4;border:1px solid #059669;border-radius:6px;padding:10px 14px;margin-bottom:8px;">
<div style="font-weight:800;color:#065f46;font-size:0.98rem;">[+] CAPITAL FEASIBLE ({plan['plan_verdict']})</div>
<div style="color:#047857;font-size:0.82rem;">Available budget ({sym}{user_budget:,.2f}) covers the pilot threshold with sufficient logistics buffer.</div>
</div>""", unsafe_allow_html=True)
    else:
        st.markdown(f"""<div style="background:#fef2f2;border:1px solid #dc2626;border-radius:6px;padding:10px 14px;margin-bottom:8px;">
<div style="font-weight:800;color:#991b1b;font-size:0.98rem;">[!] CAPITAL CONSTRAINED ({plan['plan_verdict']})</div>
<div style="color:#b91c1c;font-size:0.82rem;">Minimum viable pilot requires {sym}{plan['min_capital_required']:,.2f} to prevent initial inventory stockouts.</div>
</div>""", unsafe_allow_html=True)

    # 2. SECONDARY CARDS: 4 Core Feasibility Metrics
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.metric(t("plan_min_capital", cur_lang), f"{sym}{plan['min_capital_required']:,.0f}")
    with k2:
        st.metric(t("plan_units", cur_lang), f"{plan['purchasable_units']:,}")
    with k3:
        st.metric(t("plan_breakeven", cur_lang), plan["break_even_timeline"])
    with k4:
        st.metric(t("plan_adjusted_prob", cur_lang), f"{plan['budget_adjusted_success_prob']:.0f}%")

    # 3. TERTIARY CARD: Allocation Breakdown
    st.caption(t("plan_alloc_title", cur_lang))
    a1, a2, a3 = st.columns(3)
    with a1:
        st.markdown(f"""<div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:10px;text-align:center;">
<strong>Procurement (55%)</strong><br/>{sym}{user_budget * 0.55:,.2f}
</div>""", unsafe_allow_html=True)
    with a2:
        st.markdown(f"""<div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:10px;text-align:center;">
<strong>Freight Buffer (25%)</strong><br/>{sym}{user_budget * 0.25:,.2f}
</div>""", unsafe_allow_html=True)
    with a3:
        st.markdown(f"""<div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:10px;text-align:center;">
<strong>Working Capital (20%)</strong><br/>{sym}{user_budget * 0.20:,.2f}
</div>""", unsafe_allow_html=True)

    st.markdown("---")
    b1, b2 = st.columns([1.5, 4])
    with b1:
        if st.button(t("btn_apply_budget", cur_lang), type="primary", use_container_width=True, key="plan_apply_btn"):
            set_app_state_val("active_screen", "DECIDE")
            st.rerun()
    with b2:
        if st.button(t("btn_back_to_decide", cur_lang), type="secondary", key="plan_back_btn"):
            set_app_state_val("active_screen", "DECIDE")
            st.rerun()