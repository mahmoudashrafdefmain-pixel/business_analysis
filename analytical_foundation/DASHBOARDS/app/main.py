"""
MAIN APPLICATION ENTRYPOINT (Sections 176-222)
Pure Top-Level Navigation, Splash Intro, Authoritative Global State.
"""

import streamlit as st
import os
import sys
from pathlib import Path

st.set_page_config(
    page_title="Market Opportunity & Decision Platform",
    page_icon="O",
    layout="wide",
    initial_sidebar_state="collapsed"
)

APP_DIR = Path(__file__).parent.resolve()
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

ENGINE_PATH = APP_DIR.parent.parent / "MODEL" / "decision_engine"
if str(ENGINE_PATH) not in sys.path:
    sys.path.insert(0, str(ENGINE_PATH))

from components.i18n import inject_layout_css, get_current_lang
from components.state import get_app_state
from components.splash import render_splash_screen
from components.navigation import render_top_navigation
from pages.decide import render_decide_screen
from pages.why import render_why_screen
from pages.pricing_success import render_pricing_screen
from pages.plan_entry import render_plan_entry_screen
from pages.market_gaps import render_market_gaps_screen
from pages.explore import render_explore_screen
from pages.static_explorer import render_static_explorer
from pages.guide import render_guide_screen

state = get_app_state()
cur_lang = get_current_lang()
inject_layout_css(lang=cur_lang)

# 1. SPLASH INTRO SCREEN (Section: Special Dark Aesthetic Intro)
if not state.get("splash_dismissed", False):
    render_splash_screen()
    st.stop()

# 2. MAIN APPLICATION (Rendered when splash dismissed)
render_top_navigation()

app_mode = state.get("mode", "DYNAMIC")
active_screen = state.get("active_screen", "DECIDE")

if active_screen == "GUIDE":
    render_guide_screen()
elif app_mode == "STATIC":
    if active_screen == "MARKET_GAPS":
        render_market_gaps_screen()
    else:
        render_static_explorer()
else:
    if active_screen == "DECIDE":
        render_decide_screen(mode="DYNAMIC")
    elif active_screen == "WHY":
        render_why_screen()
    elif active_screen == "PRICING":
        render_pricing_screen()
    elif active_screen == "PLAN_ENTRY":
        render_plan_entry_screen()
    elif active_screen == "MARKET_GAPS":
        render_market_gaps_screen()
    elif active_screen == "WHAT_IF":
        render_explore_screen()
    else:
        render_decide_screen(mode="DYNAMIC")

st.markdown("<hr style='margin-top:10px;margin-bottom:6px;border:0;border-top:1px solid #e2e8f0;'>", unsafe_allow_html=True)
st.markdown(
    f"<div style='text-align:center;color:#94a3b8;font-size:0.75rem;'>"
    f"Product Market Entry Platform | Mode: <strong>{app_mode}</strong> | "
    f"Language: <strong>{cur_lang.upper()}</strong> | Audited Decision Engine</div>",
    unsafe_allow_html=True
)