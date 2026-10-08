"""
MODE TRANSITION ANIMATION COMPONENT (Section 68, 69)
Lightweight, subtle CSS/JS transition animation (~500ms).
"""

import streamlit as st
import time

TRANSITION_CSS = """
<style>
/* Clean, quiet typography and layout */
.main-title {
    font-size: 1.6rem;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 0.2rem;
}
.sub-title {
    font-size: 0.95rem;
    color: #64748b;
    margin-bottom: 1.2rem;
}
/* Mode Switcher Top Bar */
.mode-bar {
    display: flex;
    justify-content: center;
    gap: 12px;
    padding: 10px 0;
    margin-bottom: 16px;
    border-bottom: 1px solid #e2e8f0;
}
/* Decision Card Styling */
.decision-card-container {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 24px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    margin: 16px 0;
}
.verdict-badge {
    font-size: 2.2rem;
    font-weight: 800;
    letter-spacing: 0.05em;
    padding: 6px 16px;
    border-radius: 8px;
    display: inline-block;
}
.verdict-ENTER { color: #166534; background: #dcfce7; }
.verdict-TEST { color: #854d0e; background: #fef9c3; }
.verdict-WATCH { color: #1e40af; background: #dbeafe; }
.verdict-AVOID { color: #991b1b; background: #fee2e2; }

/* Transition Overlay */
.mode-transition-overlay {
    position: fixed;
    top: 0; left: 0; width: 100vw; height: 100vh;
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(4px);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 99999;
    animation: fadeOut 0.5s ease-out forwards;
}
.mode-transition-text {
    font-size: 2.2rem;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: 0.15em;
    padding: 12px 28px;
    background: #f1f5f9;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
}
@keyframes fadeOut {
    0% { opacity: 1; }
    70% { opacity: 1; }
    100% { opacity: 0; visibility: hidden; }
}
</style>
"""

def inject_styles():
    st.markdown(TRANSITION_CSS, unsafe_allow_html=True)

def show_mode_transition(target_mode: str):
    """Displays the subtle 500ms mode transition overlay."""
    inject_styles()
    placeholder = st.empty()
    placeholder.markdown(f"""
    <div class="mode-transition-overlay">
        <div class="mode-transition-text">{target_mode.upper()}</div>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(0.4)
    placeholder.empty()
