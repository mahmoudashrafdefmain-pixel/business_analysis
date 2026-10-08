"""
PERSISTENT TOP NAVIGATION BAR (Clean SaaS Header, Intro Replay)
"""

import streamlit as st
from components.i18n import t, get_current_lang, set_lang
from components.state import get_app_state, set_app_state_val

def render_top_navigation():
    state = get_app_state()
    cur_lang = get_current_lang()
    cur_mode = state.get("mode", "DYNAMIC")
    cur_screen = state.get("active_screen", "DECIDE")
    
    # 1. HEADER ROW: Brand on left, Language Switcher and Intro on right
    h_col1, h_col2 = st.columns([4, 1.6])
    with h_col1:
        st.markdown(f"""<div style="font-size:1.15rem;font-weight:800;color:#0f172a;letter-spacing:-0.01em;">
{t("app_title", cur_lang)}
</div>""", unsafe_allow_html=True)
        
    with h_col2:
        lang_btn_cols = st.columns(3)
        with lang_btn_cols[0]:
            if st.button("English", type="primary" if cur_lang == "en" else "secondary", use_container_width=True, key="btn_lang_en"):
                set_lang("en")
                set_app_state_val("lang", "en")
                st.rerun()
        with lang_btn_cols[1]:
            if st.button("العربية", type="primary" if cur_lang == "ar" else "secondary", use_container_width=True, key="btn_lang_ar"):
                set_lang("ar")
                set_app_state_val("lang", "ar")
                st.rerun()
        with lang_btn_cols[2]:
            home_label = t("nav_home", cur_lang)
            if st.button(home_label, type="secondary", use_container_width=True, key="btn_replay_home"):
                state["splash_dismissed"] = False
                st.rerun()

    # 2. NAVIGATION BAR ROW
    m_col, s_col, g_col = st.columns([1.3, 5.2, 0.9])
    
    with m_col:
        mb1, mb2 = st.columns(2)
        with mb1:
            if st.button(t("mode_static", cur_lang), type="primary" if cur_mode == "STATIC" else "secondary", use_container_width=True, key="nav_mode_static"):
                set_app_state_val("mode", "STATIC")
                set_app_state_val("active_screen", "STATIC_EXPLORER")
                st.rerun()
        with mb2:
            if st.button(t("mode_dynamic", cur_lang), type="primary" if cur_mode == "DYNAMIC" else "secondary", use_container_width=True, key="nav_mode_dynamic"):
                set_app_state_val("mode", "DYNAMIC")
                if cur_screen == "STATIC_EXPLORER":
                    set_app_state_val("active_screen", "DECIDE")
                st.rerun()

    with s_col:
        if cur_mode == "DYNAMIC":
            dyn_screens = [
                ("DECIDE", t("nav_decide", cur_lang)),
                ("WHY", t("nav_why", cur_lang)),
                ("PRICING", t("nav_pricing", cur_lang)),
                ("PLAN_ENTRY", t("nav_plan_entry", cur_lang)),
                ("MARKET_GAPS", t("nav_market_gaps", cur_lang)),
                ("WHAT_IF", t("nav_what_if", cur_lang))
            ]
            scr_cols = st.columns(len(dyn_screens))
            for idx, (s_key, s_label) in enumerate(dyn_screens):
                with scr_cols[idx]:
                    is_active = (cur_screen == s_key)
                    if st.button(s_label, type="primary" if is_active else "secondary", use_container_width=True, key=f"nav_dyn_{s_key}"):
                        set_app_state_val("active_screen", s_key)
                        st.rerun()
        else:
            stat_screens = [
                ("STATIC_EXPLORER", t("nav_overview", cur_lang)),
                ("MARKET_GAPS", t("nav_market_gaps", cur_lang))
            ]
            stat_cols = st.columns(2)
            for idx, (s_key, s_label) in enumerate(stat_screens):
                with stat_cols[idx]:
                    is_active = (cur_screen == s_key)
                    if st.button(s_label, type="primary" if is_active else "secondary", use_container_width=True, key=f"nav_stat_{s_key}"):
                        set_app_state_val("active_screen", s_key)
                        st.rerun()

    with g_col:
        is_guide_active = (cur_screen == "GUIDE")
        if st.button(t("nav_guide", cur_lang), type="primary" if is_guide_active else "secondary", use_container_width=True, key="nav_btn_guide"):
            set_app_state_val("active_screen", "GUIDE")
            st.rerun()

    st.markdown("<hr style='margin-top:4px;margin-bottom:8px;border:0;border-top:1px solid #cbd5e1;'>", unsafe_allow_html=True)