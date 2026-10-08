"""
PAGE 5: MARKET GAPS SCREEN (Flush-Left HTML, State-Synchronized)
"""

import streamlit as st
from components.i18n import t, get_current_lang
from components.state import get_analysis_bundle, set_app_state_val

def render_market_gaps_screen():
    cur_lang = get_current_lang()
    bundle = get_analysis_bundle()
    gaps = bundle["market_gaps"]
    markets = gaps["markets_summary"]
    df_matrix = gaps["product_market_matrix"]

    st.markdown(f"""<div style="font-size:1.25rem;font-weight:800;color:#0f172a;margin-bottom:2px;">
{t("gaps_title", cur_lang)}
</div>
<div style="font-size:0.82rem;color:#64748b;margin-bottom:8px;">
{t("gaps_sub", cur_lang)}
</div>""", unsafe_allow_html=True)

    # 1. PRIMARY CARDS: 5 Market Profiles Grid
    for m in markets:
        with st.expander(f"Market: {m['market']} (Score: {m['opportunity_score']}/100)", expanded=False):
            c_info, c_btn = st.columns([3.5, 1])
            with c_info:
                st.markdown(f"""<strong>{t('gaps_strongest', cur_lang)}:</strong> {m['strongest_need']}<br/>
<strong>{t('gaps_potential', cur_lang)}:</strong> {m['potential_gaps']}<br/>
<strong>{t('gaps_lower', cur_lang)}:</strong> {m['lower_opportunity']}<br/>
<strong>{t('gaps_risk', cur_lang)}:</strong> {m['main_risk']}<br/>
<strong>{t('gaps_strategy', cur_lang)}:</strong> {m['recommended_direction']}""", unsafe_allow_html=True)
            with c_btn:
                if st.button(f"Select {m['market'][:10]}", key=f"sel_m_{m['market']}", use_container_width=True):
                    m_clean = "United States" if "United States" in m['market'] else                               "Brazil" if "Brazil" in m['market'] else                               "United Kingdom" if "United Kingdom" in m['market'] else "Germany"
                    set_app_state_val("market", m_clean)
                    set_app_state_val("active_screen", "DECIDE")
                    st.rerun()

    # 2. SECONDARY CARD: Product-Market Opportunity Matrix
    st.caption(t('gaps_matrix_title', cur_lang))
    st.dataframe(df_matrix.set_index("Product Category"), use_container_width=True)

    st.markdown("---")
    if st.button(t("btn_back_to_decide", cur_lang), type="primary", key="gaps_back_btn"):
        set_app_state_val("active_screen", "DECIDE")
        st.rerun()