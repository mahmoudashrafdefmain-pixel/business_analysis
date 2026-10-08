"""
INTERNATIONALIZATION & LOCALIZATION ENGINE (Sections 139-148)
First-Class Bilingual Support: English (en) & Arabic / العربية (ar).
Natural modern business Arabic, LTR/RTL layout switching, and currency localization.
"""

import streamlit as st

TRANSLATIONS = {
    # Brand & Navigation
    "app_title": {
        "en": "Market Opportunity & Decision Platform",
        "ar": "منصة فرص السوق وقرارات الدخول التجارية"
    },
    "app_subtitle": {
        "en": "Audited Decision Engine | 4 Calibrated RF Models",
        "ar": "محرك القرارات المعتمد | 4 نماذج غابات عشوائية معايرة"
    },
    "mode_platform": {
        "en": "MODE",
        "ar": "وضع المنصة"
    },
    "mode_static": {
        "en": "Static",
        "ar": "ثابت"
    },
    "mode_dynamic": {
        "en": "Dynamic",
        "ar": "تفاعلي"
    },
    "nav_screens": {
        "en": "SCREENS",
        "ar": "الشاشات"
    },
    "nav_home": {
        "en": "Home",
        "ar": "الرئيسية"
    },
    "nav_decide": {
        "en": "Decide",
        "ar": "القرار"
    },
    "nav_why": {
        "en": "Why?",
        "ar": "المبررات"
    },
    "nav_pricing": {
        "en": "Price & Success",
        "ar": "السعر والنجاح"
    },
    "nav_plan_entry": {
        "en": "Plan My Entry",
        "ar": "خطة الدخول"
    },
    "nav_market_gaps": {
        "en": "Market Gaps",
        "ar": "فجوات السوق"
    },
    "nav_what_if": {
        "en": "What-If",
        "ar": "المحاكاة"
    },
    "nav_guide": {
        "en": "Guide",
        "ar": "الدليل"
    },
    "nav_overview": {
        "en": "Market Overview",
        "ar": "نظرة عامة على السوق"
    },
    "nav_switch_to_dynamic": {
        "en": "Switch to Dynamic Mode",
        "ar": "الانتقال للوضع التفاعلي"
    },

    # Decision Page
    "decide_headline": {
        "en": "Should I enter this product into this market?",
        "ar": "هل يجب أن أطرح هذا المنتج في هذا السوق؟"
    },
    "decide_subheadline": {
        "en": "Evaluate market traction, calibrated machine learning success probability, and unit economics to deliver ONE clear verdict.",
        "ar": "تقييم جاذبية السوق، واحتمالية النجاح عبر نماذج التعلم الآلي المعايرة، واقتصاديات الوحدة لإصدار قرار حاسم وموثوق."
    },
    "scope_label": {
        "en": "1. Analytical Scope & Model System",
        "ar": "1. النطاق التحليلي ونظام النموذج"
    },
    "scope_all": {
        "en": "Harmonized Catalog (ALL DATASETS - Cross-Market RF)",
        "ar": "الكتالوج الموحد (كافة مجموعات البيانات - نموذج عابر للأسواق)"
    },
    "scope_olist": {
        "en": "Olist Marketplace (Brazil - Delivery & Logistics RF)",
        "ar": "منصة أولست (البرازيل - نموذج كفاءة التوصيل واللوجستيات)"
    },
    "scope_gs": {
        "en": "Global Superstore (Worldwide - Commercial Profit RF)",
        "ar": "جلوبال سوبرستور (عالمي - نموذج هوامش الربحية التجارية)"
    },
    "scope_uci": {
        "en": "UCI Online Retail II (UK - Wholesale & Repeat Rate RF)",
        "ar": "يو سي آي لتجارة التجزئة (بريطانيا - نموذج مبيعات الجملة والتكرار)"
    },
    "search_title": {
        "en": "Search Product (Keyword, Name, or SKU)",
        "ar": "البحث عن منتج (بالكلمة المفتاحية، الاسم، أو الرمز)"
    },
    "search_placeholder": {
        "en": "Type 'clock', 'desk', 'decor', or SKU...",
        "ar": "اكتب 'clock' أو 'desk' أو 'decor' أو رمز المنتج..."
    },
    "search_caption": {
        "en": "Partial match & keyword rank across 48,548 catalog products",
        "ar": "مطابقة جزئية وتصنيف بالكلمات المفتاحية عبر 48,548 منتجاً"
    },
    "select_product_label": {
        "en": "Select Product to Analyze",
        "ar": "اختر المنتج للتحليل"
    },
    "market_label": {
        "en": "2. Target Market",
        "ar": "2. السوق المستهدف"
    },
    "city_label": {
        "en": "3. Target City (Optional)",
        "ar": "3. المدينة المستهدفة (اختياري)"
    },
    "city_none": {
        "en": "National / Regional Average",
        "ar": "المتوسط الوطني / الإقليمي العام"
    },
    "budget_label": {
        "en": "4. Capital Budget ($)",
        "ar": "4. رأس المال المتاح ($)"
    },
    "target_price_label": {
        "en": "5. Target Price (0 for auto)",
        "ar": "5. السعر المستهدف (0 للتلقائي)"
    },
    "btn_analyze": {
        "en": "ANALYZE OPPORTUNITY NOW",
        "ar": "تحليل الفرصة الاستثمارية الآن"
    },
    "analyzing_spinner": {
        "en": "Executing calibrated Random Forest inference and evaluating market parameters...",
        "ar": "جاري تشغيل نموذج الغابات العشوائية المعاير وتقييم معايير السوق..."
    },

    # Decision Card
    "card_opportunity_score": {
        "en": "Opportunity Score",
        "ar": "درجة الفرصة في السوق"
    },
    "card_success_prob": {
        "en": "Model Success Probability",
        "ar": "احتمالية النجاح المقدرة"
    },
    "card_rec_price": {
        "en": "Recommended Price",
        "ar": "السعر المقترح"
    },
    "card_model_used": {
        "en": "Model",
        "ar": "النموذج المستخدم"
    },
    "card_product": {
        "en": "Product",
        "ar": "المنتج"
    },
    "card_category": {
        "en": "Category",
        "ar": "الفئة"
    },
    "card_indicators_title": {
        "en": "FIVE CORE DECISION INDICATORS",
        "ar": "المؤشرات الخمسة الأساسية للقرار"
    },
    "ind_opportunity": {
        "en": "1. Opportunity",
        "ar": "1. درجة الفرصة"
    },
    "ind_demand": {
        "en": "2. Demand",
        "ar": "2. الطلب التجاري"
    },
    "ind_success": {
        "en": "3. Success Prob",
        "ar": "3. احتمالية النجاح"
    },
    "ind_economics": {
        "en": "4. Economics",
        "ar": "4. اقتصاديات الوحدة"
    },
    "ind_risk": {
        "en": "5. Risk",
        "ar": "5. مستوى المخاطر"
    },
    "card_actions_title": {
        "en": "Recommended Next Actions",
        "ar": "الإجراءات والخطوات الموصى بها"
    },
    "btn_view_why": {
        "en": "View WHY Breakdown",
        "ar": "عرض مبررات القرار بالتفصيل"
    },
    "btn_view_pricing": {
        "en": "Price & Success Curve",
        "ar": "منحنى السعر والنجاح"
    },
    "btn_view_plan": {
        "en": "Plan My Entry (Budget)",
        "ar": "خطة الدخول ورأس المال"
    },
    "btn_view_markets": {
        "en": "Explore All Markets",
        "ar": "استكشاف كافة الأسواق"
    },
    "btn_back_to_decide": {
        "en": "Back to Decision Card",
        "ar": "العودة لبطاقة القرار"
    },

    # Verdicts
    "verdict_ENTER": {
        "en": "ENTER",
        "ar": "دخول السوق"
    },
    "verdict_TEST": {
        "en": "TEST",
        "ar": "اختبار تجريبي"
    },
    "verdict_WATCH": {
        "en": "WATCH",
        "ar": "مراقبة السوق"
    },
    "verdict_AVOID": {
        "en": "AVOID",
        "ar": "تجنب الدخول"
    },

    # Why Page
    "why_title": {
        "en": "Why this Decision:",
        "ar": "مبررات وأسباب القرار:"
    },
    "why_final_reason_title": {
        "en": "SYNTHESIZED FINAL REASON",
        "ar": "الخلاصة التنفيذية للقرار"
    },
    "why_supports_title": {
        "en": "What Supports Market Entry",
        "ar": "العوامل الداعمة لدخول السوق"
    },
    "why_hurts_title": {
        "en": "What Hurts or Poses Risk",
        "ar": "عوامل الخطر والتحذيرات"
    },
    "why_evidence_title": {
        "en": "Empirical Evidence Pillars",
        "ar": "ركائز الأدلة والبيانات التجريبية"
    },

    # Pricing Page
    "pricing_title": {
        "en": "Price Intelligence & Sensitivity Curve",
        "ar": "ذكاء التسعير ومنحنى حساسية النجاح"
    },
    "pricing_sub": {
        "en": "Evaluate how product success probability dynamically responds to price changes.",
        "ar": "تحليل كيفية تغير احتمالية نجاح المنتج ديناميكياً مع تعديل سعر البيع."
    },
    "pricing_rec_range": {
        "en": "Recommended Price Range",
        "ar": "نطاق السعر المقترح"
    },
    "pricing_optimal": {
        "en": "Optimal Baseline Price",
        "ar": "السعر الأساسي المثالي"
    },
    "pricing_scope": {
        "en": "Pricing Evidence Scope",
        "ar": "نطاق دليل التسعير"
    },
    "pricing_slider_label": {
        "en": "Simulate Target Selling Price",
        "ar": "محاكاة سعر البيع المستهدف"
    },
    "btn_apply_price": {
        "en": "Apply Price & Update Decision",
        "ar": "اعتماد السعر وتحديث القرار"
    },

    # Plan Entry Page
    "plan_title": {
        "en": "Plan My Entry: Capital Feasibility",
        "ar": "تخطيط الدخول: الجدوى المالية ورأس المال"
    },
    "plan_sub": {
        "en": "Determine whether your capital budget realistically supports pilot inventory and market expansion.",
        "ar": "تحديد مدى قدرة ميزانيتك المالية على تغطية الدفعة التجريبية الأولى والتوسع بالسوق."
    },
    "plan_min_capital": {
        "en": "Min. Pilot Capital",
        "ar": "الحد الأدنى لرأس المال"
    },
    "plan_units": {
        "en": "Purchasable Pilot Units",
        "ar": "الوحدات القابلة للشراء"
    },
    "plan_breakeven": {
        "en": "Break-Even Timeline",
        "ar": "أفق نقطة التعادل"
    },
    "plan_adjusted_prob": {
        "en": "Budget-Adjusted Success",
        "ar": "احتمالية النجاح وفق الميزانية"
    },
    "plan_alloc_title": {
        "en": "Budget Allocation Breakdown",
        "ar": "توزيع الميزانية المقترحة"
    },
    "btn_apply_budget": {
        "en": "Apply Budget & Return to Decision",
        "ar": "اعتماد الميزانية والعودة للقرار"
    },

    # Market Gaps Page
    "gaps_title": {
        "en": "Explore All Markets: Market Gaps & Opportunities",
        "ar": "استكشاف كافة الأسواق: الفجوات والفرص"
    },
    "gaps_sub": {
        "en": "Cross-market diagnostic showing empirical market gaps, products needed, and lower-opportunity areas.",
        "ar": "تشخيص عابر للأسواق يوضح الفجوات الحقيقية والمنتجات المطلوبة والمجالات المنخفضة الجدوى."
    },
    "gaps_strongest": {
        "en": "Strongest Need",
        "ar": "الاحتياج الأكثر طلباً"
    },
    "gaps_potential": {
        "en": "Potential Market Gaps",
        "ar": "فجوات السوق المحتملة"
    },
    "gaps_lower": {
        "en": "Lower Opportunity (Avoid)",
        "ar": "مجالات منخفضة الفرص (تجنبها)"
    },
    "gaps_risk": {
        "en": "Main Risk Factor",
        "ar": "عامل الخطر الرئيسي"
    },
    "gaps_strategy": {
        "en": "Strategic Direction",
        "ar": "التوجه الاستراتيجي"
    },
    "gaps_matrix_title": {
        "en": "Product-Market Opportunity Matrix (Scores / 100)",
        "ar": "مصفوفة فرص المنتجات والأسواق (الدرجات من 100)"
    },

    # What-If Page
    "explore_title": {
        "en": "What-If Simulator & Margin Sensitivity",
        "ar": "محاكاة السيناريوهات وحساسية هوامش الربح"
    },
    "explore_sub": {
        "en": "Simulate how adjustments in procurement cost, selling price, and sales volume impact net profitability.",
        "ar": "محاكاة تأثير تغييرات تكلفة التوريد وسعر البيع وحجم المبيعات على صافي الأرباح."
    },
    "explore_chart1_title": {
        "en": "1. How does margin respond to procurement cost fluctuations?",
        "ar": "1. كيف يستجيب هامش الربح لتغيرات تكلفة التوريد؟"
    },
    "explore_chart2_title": {
        "en": "2. How does net profit scale with monthly sales volume?",
        "ar": "2. كيف يتدرج صافي الربح مع نمو حجم المبيعات الشهري؟"
    },

    # Static Explorer
    "static_title": {
        "en": "Precomputed Executive Market Intelligence (Static Mode)",
        "ar": "ذكاء السوق التنفيذي المحسوب مسبقاً (الوضع الثابت)"
    },
    "static_sub": {
        "en": "Instant high-level strategic intelligence across 3 audited global datasets and 48,548 reconciled products. Zero user input required.",
        "ar": "معلومات استراتيجية فورية وشاملة عبر 3 مجموعات بيانات عالمية و48,548 منتجاً مدققاً. لا يتطلب أي إدخال مسبق."
    },
    "static_ranking_title": {
        "en": "Global Market Opportunity Ranking",
        "ar": "تصنيف جاذبية الأسواق العالمية"
    },
    "static_insights_title": {
        "en": "20 Automatically Selected Major Insights",
        "ar": "20 رؤية تحليلية تنفيذية مختارة آلياً"
    },
    "static_jump_title": {
        "en": "Jump to Dynamic Evaluation",
        "ar": "الانتقال للتحليل التفاعلي المخصص"
    },

    # Guide
    "guide_title": {
        "en": "Platform Functional Guide",
        "ar": "دليل استخدام المنصة الشامل"
    },
    "guide_sub": {
        "en": "Comprehensive card-based walkthrough explaining every function, metric, decision rule, and analytical limit.",
        "ar": "دليل توضيحي شامل عبر بطاقات مقسمة يشرح كل وظيفة، ومؤشر، وقاعدة قرار، والحدود الإحصائية للمنصة."
    }
}

def t(key: str, lang: str = "en") -> str:
    """Retrieves localized text for given key and language."""
    entry = TRANSLATIONS.get(key, {})
    return entry.get(lang, entry.get("en", key))

def get_current_lang() -> str:
    """Returns active language from session state."""
    return st.session_state.get("app_lang", "en")

def set_lang(new_lang: str):
    """Sets active language."""
    if new_lang in ["en", "ar"]:
        st.session_state["app_lang"] = new_lang

def inject_layout_css(lang: str = "en"):
    """
    Injects professional CSS ensuring:
    1. Complete sidebar suppression (Section 133).
    2. Zero traditional vertical scrolling layout with compact cards (Sections 134-138).
    3. Proper RTL / LTR typography and alignment (Sections 143-144).
    4. Minimalist business SaaS styling with zero emojis (Sections 156-161).
    """
    is_rtl = (lang == "ar")
    direction = "rtl" if is_rtl else "ltr"
    align = "right" if is_rtl else "left"
    font_family = "'Segoe UI', 'Cairo', -apple-system, BlinkMacSystemFont, Tahoma, sans-serif"

    css = f"""
    <style>
        /* 1. STRICT SIDEBAR SUPPRESSION (Section 133) */
        [data-testid="stSidebar"], 
        [data-testid="collapsedControl"], 
        header[data-testid="stHeader"] {{
            display: none !important;
            visibility: hidden !important;
        }}

        /* 2. ROOT & BODY STYLING */
        html, body, [data-testid="stAppViewContainer"] {{
            direction: {direction};
            text-align: {align};
            font-family: {font_family};
            background-color: #f8fafc;
            color: #0f172a;
        }}

        /* 3. COMPACT NO-SCROLL CONTAINER */
        .block-container {{
            padding-top: 0.6rem !important;
            padding-bottom: 0.8rem !important;
            padding-left: 1.0rem !important;
            padding-right: 1.0rem !important;
            max-width: 1360px !important;
        }}

        /* 4. TYPOGRAPHY HIERARCHY */
        h1, h2, h3, h4, h5 {{
            font-family: {font_family};
            font-weight: 700;
            color: #0f172a;
            margin-top: 0.15rem;
            margin-bottom: 0.35rem;
        }}
        h2 {{ font-size: 1.30rem !important; }}
        h3 {{ font-size: 1.05rem !important; }}
        h4 {{ font-size: 0.90rem !important; }}

        /* 5. METRIC BLOCKS */
        div[data-testid="stMetricValue"] {{
            font-size: 1.30rem !important;
            font-weight: 800 !important;
            color: #0f172a !important;
        }}
        div[data-testid="stMetricLabel"] {{
            font-size: 0.75rem !important;
            font-weight: 600 !important;
            color: #64748b !important;
            text-transform: uppercase;
        }}

        /* 6. BUTTON STYLING (Subtle, professional SaaS) */
        button[kind="primary"], button[kind="secondary"] {{
            font-family: {font_family};
            border-radius: 6px !important;
            font-size: 0.80rem !important;
            font-weight: 600 !important;
            padding: 0.30rem 0.65rem !important;
            transition: all 0.2s ease-in-out;
        }}
        button[kind="primary"] {{
            background-color: #0f172a !important;
            color: #ffffff !important;
            border: 1px solid #0f172a !important;
        }}
        button[kind="primary"]:hover {{
            background-color: #1e293b !important;
        }}
        button[kind="secondary"] {{
            background-color: #ffffff !important;
            color: #334155 !important;
            border: 1px solid #cbd5e1 !important;
        }}
        button[kind="secondary"]:hover {{
            background-color: #f1f5f9 !important;
            border-color: #94a3b8 !important;
        }}

        /* 7. CARD PANELS */
        .platform-card {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 12px 14px;
            margin-bottom: 8px;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.04);
        }}

        /* 8. FORM CONTROLS COMPACT */
        .stSelectbox, .stTextInput, .stNumberInput, .stSlider {{
            margin-bottom: 0.15rem !important;
        }}
        div[data-baseweb="select"] > div {{
            min-height: 34px !important;
            font-size: 0.85rem !important;
        }}

        /* Subtle smooth transition */
        * {{
            transition: background-color 0.15s ease, color 0.15s ease;
        }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)