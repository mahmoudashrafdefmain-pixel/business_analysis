"""
SPLASH INTRO ANIMATION (Professional Dark Aesthetics)
Black, White, Crimson Red palette.
4-Word Title: GLOBAL MARKET DECISION INTELLIGENCE.
Center Geometric Nexus Logo with Pulse Animation.
"""

import streamlit as st
from components.i18n import get_current_lang

def render_splash_screen():
    lang = get_current_lang()
    enter_label = "ENTER PLATFORM" if lang == "en" else "دخول المنصة"
    
    splash_html = """<style>
.splash-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 75vh;
    background: #050505;
    color: #ffffff;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    border-radius: 12px;
    padding: 50px 20px;
    text-align: center;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.95);
    border: 1px solid #1f1f1f;
    animation: splashFadeIn 0.8s ease-out;
}
@keyframes splashFadeIn {
    from { opacity: 0; transform: scale(0.97); }
    to { opacity: 1; transform: scale(1.0); }
}
@keyframes nexusPulse {
    0% { transform: scale(0.96); filter: drop-shadow(0 0 10px rgba(220, 38, 38, 0.4)); }
    50% { transform: scale(1.06); filter: drop-shadow(0 0 30px rgba(220, 38, 38, 0.85)); }
    100% { transform: scale(0.96); filter: drop-shadow(0 0 10px rgba(220, 38, 38, 0.4)); }
}
.splash-icon {
    width: 120px;
    height: 120px;
    margin-bottom: 24px;
    animation: nexusPulse 3s infinite ease-in-out;
}
.splash-title {
    font-size: 2.3rem;
    font-weight: 900;
    letter-spacing: 0.08em;
    color: #ffffff;
    text-transform: uppercase;
    margin-bottom: 12px;
    line-height: 1.2;
}
.splash-red-bar {
    width: 90px;
    height: 4px;
    background: #dc2626;
    margin: 14px auto 22px auto;
    border-radius: 2px;
    box-shadow: 0 0 12px rgba(220, 38, 38, 0.8);
}
.splash-sub {
    font-size: 0.95rem;
    color: #a3a3a3;
    max-width: 650px;
    line-height: 1.6;
    margin-bottom: 36px;
    letter-spacing: 0.02em;
}
</style>
<div class="splash-wrapper">
    <svg class="splash-icon" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="50" cy="50" r="46" stroke="#262626" stroke-width="2"/>
        <circle cx="50" cy="50" r="36" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="6 4"/>
        <polygon points="50,18 78,34 78,66 50,82 22,66 22,34" stroke="#ffffff" stroke-width="2" fill="none"/>
        <circle cx="50" cy="50" r="10" fill="#dc2626"/>
        <circle cx="50" cy="4" r="4" fill="#ffffff"/>
        <line x1="50" y1="4" x2="50" y2="18" stroke="#dc2626" stroke-width="3"/>
        <line x1="50" y1="82" x2="50" y2="96" stroke="#dc2626" stroke-width="3"/>
        <line x1="4" y1="50" x2="18" y2="50" stroke="#dc2626" stroke-width="3"/>
        <line x1="82" y1="50" x2="96" y2="50" stroke="#dc2626" stroke-width="3"/>
    </svg>
    <div class="splash-title">
        GLOBAL MARKET DECISION INTELLIGENCE
    </div>
    <div class="splash-red-bar"></div>
    <div class="splash-sub">
        Audited Commercial Demand | Unit Economics Feasibility | Calibrated Predictive Machine Learning
    </div>
</div>"""

    st.markdown(splash_html, unsafe_allow_html=True)

    col_l, col_btn, col_r = st.columns([2.5, 2, 2.5])
    with col_btn:
        if st.button(enter_label, type="primary", use_container_width=True, key="btn_dismiss_splash"):
            st.session_state["app_state"]["splash_dismissed"] = True
            st.rerun()
