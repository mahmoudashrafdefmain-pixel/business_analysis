"""
SMART PRODUCT SEARCH BAR COMPONENT (Sections 88-90, 156-160)
Case-insensitive partial matching, keyword-ranked catalog lookup. Zero emojis.
"""

import streamlit as st
import sys
from pathlib import Path

ENGINE_PATH = Path(__file__).resolve().parents[2] / "MODEL" / "decision_engine"
if str(ENGINE_PATH) not in sys.path:
    sys.path.insert(0, str(ENGINE_PATH))

from calculations import search_products
from components.i18n import t, get_current_lang

def render_search_bar(dataset_key: str = "all_datasets", default_sku: str = None):
    cur_lang = get_current_lang()
    
    col_input, col_info = st.columns([3.2, 1.3])
    with col_input:
        search_query = st.text_input(
            t("search_title", cur_lang),
            value=st.session_state.get("search_query", ""),
            placeholder=t("search_placeholder", cur_lang),
            key="product_search_input",
            label_visibility="collapsed"
        )
    with col_info:
        st.caption(t("search_caption", cur_lang))

    matches = search_products(query=search_query, dataset_key=dataset_key, limit=20)
    if not matches:
        matches = search_products(query="", dataset_key=dataset_key, limit=20)

    sku_list = [m["original_product_id"] for m in matches]
    label_map = {
        m["original_product_id"]: f"{m['product_name'][:45]} | {m['category'][:20]} | {m['orders']} orders [SKU: {m['original_product_id']}]"
        for m in matches
    }
    
    cur_selected = st.session_state.get("selected_product", default_sku or (sku_list[0] if sku_list else None))
    default_idx = 0
    if cur_selected in sku_list:
        default_idx = sku_list.index(cur_selected)
        
    selected_sku = st.selectbox(
        t("select_product_label", cur_lang),
        options=sku_list,
        index=default_idx,
        format_func=lambda x: label_map.get(x, x),
        key="product_select_dropdown",
        label_visibility="collapsed"
    )
    
    st.session_state["selected_product"] = selected_sku
    selected_item = next((m for m in matches if m["original_product_id"] == selected_sku), matches[0] if matches else None)
    return selected_item