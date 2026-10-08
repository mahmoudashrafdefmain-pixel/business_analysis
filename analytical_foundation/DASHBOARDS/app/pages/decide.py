"""
PAGE 1: DECIDE SCREEN (Pure Dynamic & Clean Pricing Mode Control)
"""

import streamlit as st
from components.i18n import t, get_current_lang
from components.search_bar import render_search_bar
from components.decision_card import render_decision_card
from components.state import get_app_state, set_app_state_val, get_analysis_bundle, invalidate_analysis

def render_decide_screen(mode: str = "DYNAMIC"):
    cur_lang = get_current_lang()
    state = get_app_state()

    st.markdown(f"""<div style="font-size:1.15rem;font-weight:800;color:#0f172a;margin-bottom:2px;">
{t("decide_headline", cur_lang)}
</div>
<div style="font-size:0.82rem;color:#64748b;margin-bottom:8px;">
{t("decide_subheadline", cur_lang)}
</div>""", unsafe_allow_html=True)

    scope_options = {
        t("scope_all", cur_lang): "all_datasets",
        t("scope_olist", cur_lang): "olist",
        t("scope_gs", cur_lang): "global_superstore",
        t("scope_uci", cur_lang): "uci_online_retail_ii"
    }
    
    # 1. SCOPE & SEARCH
    p_c1, p_c2 = st.columns([2.5, 3.5])
    with p_c1:
        rev_scope = {v: k for k, v in scope_options.items()}
        cur_scope_label = rev_scope.get(state["dataset_key"], list(scope_options.keys())[0])
        sel_scope_label = st.selectbox(
            t("scope_label", cur_lang),
            options=list(scope_options.keys()),
            index=list(scope_options.keys()).index(cur_scope_label),
            key="scope_select"
        )
        new_dataset_key = scope_options[sel_scope_label]
        if new_dataset_key != state["dataset_key"]:
            set_app_state_val("dataset_key", new_dataset_key)
            st.rerun()
        
    with p_c2:
        selected_prod = render_search_bar(dataset_key=state["dataset_key"], default_sku=state["product_id"])
        if selected_prod and selected_prod["original_product_id"] != state["product_id"]:
            set_app_state_val("product_id", selected_prod["original_product_id"])
            st.rerun()

    # 2. PARAMETERS: Market, City, Budget, Pricing Mode
    g1, g2, g3 = st.columns(3)
    with g1:
        markets = ["United States", "Brazil", "United Kingdom", "Germany", "France", "Australia", "Global Cross-Market"]
        cur_m = state.get("market", "United States")
        m_idx = markets.index(cur_m) if cur_m in markets else 0
        new_market = st.selectbox(t("market_label", cur_lang), markets, index=m_idx, key="market_select")
        if new_market != state["market"]:
            set_app_state_val("market", new_market)
            st.rerun()

    with g2:
        cities = [t("city_none", cur_lang), "New York", "Los Angeles", "Chicago", "London", "São Paulo", "Rio de Janeiro"]
        cur_c = state.get("city") or t("city_none", cur_lang)
        c_idx = cities.index(cur_c) if cur_c in cities else 0
        new_city_label = st.selectbox(t("city_label", cur_lang), cities, index=c_idx, key="city_select")
        new_city = None if new_city_label == t("city_none", cur_lang) else new_city_label
        if new_city != state["city"]:
            set_app_state_val("city", new_city)
            st.rerun()

    with g3:
        new_budget = st.number_input(t("budget_label", cur_lang), value=float(state.get("budget", 5000.0)), step=1000.0, key="budget_input")
        if new_budget != state["budget"]:
            set_app_state_val("budget", new_budget)
            st.rerun()

    # 3. CLEAN PRICING MODE CONTROL (Section 188)
    pr_col1, pr_col2 = st.columns([2, 2])
    with pr_col1:
        pricing_modes = ["auto", "custom"]
        pricing_labels = {
            "auto": "Automatic Recommended Price" if cur_lang == "en" else "السعر المقترح تلقائياً",
            "custom": "Enter Custom Target Price" if cur_lang == "en" else "إدخال سعر مستهدف مخصص"
        }
        cur_pm = state.get("pricing_mode", "auto")
        sel_pm = st.radio(
            "Pricing Mode" if cur_lang == "en" else "وضع التسعير",
            options=pricing_modes,
            index=0 if cur_pm == "auto" else 1,
            format_func=lambda x: pricing_labels.get(x, x),
            horizontal=True,
            key="pricing_mode_radio"
        )
        if sel_pm != state["pricing_mode"]:
            set_app_state_val("pricing_mode", sel_pm)
            st.rerun()

    with pr_col2:
        if sel_pm == "custom":
            cur_cp = float(state.get("custom_price") or 50.0)
            new_cp = st.number_input(
                "Custom Unit Price" if cur_lang == "en" else "سعر الوحدة المخصص",
                value=cur_cp,
                step=5.0,
                key="custom_price_val"
            )
            if new_cp != state.get("custom_price"):
                set_app_state_val("custom_price", new_cp)
                st.rerun()
        else:
            bundle_temp = get_analysis_bundle()
            rec_p = bundle_temp["price_recommendation"]
            st.info(f"Using empirical price: {rec_p.get('formatted_range')} ({rec_p.get('evidence_level')})")

    # Primary Analyze Button (Refreshes Analysis)
    if st.button(t("btn_analyze", cur_lang), type="primary", use_container_width=True, key="btn_analyze_main"):
        invalidate_analysis()
        st.rerun()

    # Authoritative Output from Single Pipeline
    bundle = get_analysis_bundle()
    render_decision_card(bundle["decision"])