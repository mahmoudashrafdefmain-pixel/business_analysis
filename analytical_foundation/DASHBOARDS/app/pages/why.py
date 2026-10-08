"""
PAGE 2: WHY SCREEN (Clean Flush-Left HTML, State-Synchronized)
"""

import streamlit as st
from components.i18n import t, get_current_lang
from components.state import get_analysis_bundle, set_app_state_val

def render_why_screen():
    cur_lang = get_current_lang()
    bundle = get_analysis_bundle()
    decision_res = bundle["decision"]
    verdict = decision_res.get("decision", "TEST")
    verdict_label = t(f"verdict_{verdict}", cur_lang)
    why_data = decision_res.get("why_breakdown", {})
    evidence_blocks = decision_res.get("evidence_blocks", [])

    st.markdown(f"""<div style="font-size:1.25rem;font-weight:800;color:#0f172a;margin-bottom:6px;">
{t("why_title", cur_lang)} <span style="color:#2563eb;">{verdict_label}</span>
</div>""", unsafe_allow_html=True)

    # 1. PRIMARY CARD: Synthesized Final Reason (Flush-left)
    final_reason_text = why_data.get("final_reason", "Analysis generated from empirical transactional data.")
    st.markdown(f"""<div style="background:#ffffff;border-left:4px solid #2563eb;border-radius:6px;padding:12px 16px;margin-bottom:8px;border-top:1px solid #e2e8f0;border-right:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0;">
<div style="font-size:0.75rem;font-weight:700;color:#2563eb;text-transform:uppercase;margin-bottom:4px;">{t("why_final_reason_title", cur_lang)}</div>
<div style="font-size:0.95rem;line-height:1.45;color:#1e293b;font-weight:500;">{final_reason_text}</div>
</div>""", unsafe_allow_html=True)

    # 2. SECONDARY CARDS: Supports vs Hurts Split
    c_supp, c_hurt = st.columns(2)
    with c_supp:
        st.markdown(f"**[+] {t('why_supports_title', cur_lang)}**")
        supports = why_data.get("supports", [])
        for s in supports:
            clean_s = s.replace("✓", "").strip()
            st.markdown(f"""<div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:6px;padding:8px 12px;margin-bottom:6px;color:#065f46;font-size:0.85rem;">
<strong>{clean_s}</strong>
</div>""", unsafe_allow_html=True)

    with c_hurt:
        st.markdown(f"**[!] {t('why_hurts_title', cur_lang)}**")
        hurts = why_data.get("hurts", [])
        for h in hurts:
            clean_h = h.replace("⚠", "").strip()
            st.markdown(f"""<div style="background:#fef2f2;border:1px solid #fecaca;border-radius:6px;padding:8px 12px;margin-bottom:6px;color:#991b1b;font-size:0.85rem;">
<strong>{clean_h}</strong>
</div>""", unsafe_allow_html=True)

    # 3. TERTIARY CARD: Empirical Evidence Pillars
    st.caption(t("why_evidence_title", cur_lang))
    p_cols = st.columns(len(evidence_blocks) if evidence_blocks else 1)
    for idx, b in enumerate(evidence_blocks):
        with p_cols[idx]:
            st.markdown(f"""<div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:8px 10px;height:100%;">
<div style="font-weight:700;font-size:0.80rem;color:#0f172a;">{b.get('title')}</div>
<div style="font-size:0.72rem;color:#2563eb;font-weight:600;">Status: {b.get('status')}</div>
<div style="font-size:0.75rem;color:#64748b;margin-top:4px;line-height:1.3;">{b.get('summary')}</div>
</div>""", unsafe_allow_html=True)

    st.markdown("---")
    if st.button(t("btn_back_to_decide", cur_lang), type="primary", key="why_back_btn"):
        set_app_state_val("active_screen", "DECIDE")
        st.rerun()