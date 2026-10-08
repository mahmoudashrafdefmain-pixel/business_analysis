"""
PAGE 8: COMPREHENSIVE CARD-BASED INTERACTIVE GUIDE (Clean Flush-Left HTML, No Duplicates)
"""

import streamlit as st
from components.i18n import t, get_current_lang
from components.state import set_app_state_val

def render_guide_screen():
    cur_lang = get_current_lang()
    is_ar = (cur_lang == "ar")
    
    st.markdown(f"""<div style="font-size:1.25rem;font-weight:800;color:#0f172a;margin-bottom:2px;">
{t("guide_title", cur_lang)}
</div>
<div style="font-size:0.82rem;color:#64748b;margin-bottom:8px;">
{t("guide_sub", cur_lang)}
</div>""", unsafe_allow_html=True)

    topics = [
        {
            "id": "1",
            "title_en": "1. Platform Purpose & Single Core Decision",
            "title_ar": "1. هدف المنصة والقرار الأساسي الموحد",
            "content_en": """**Primary Decision**: *"Should I enter this product into this market?"*
The platform eliminates dashboard clutter by mapping historical transactions, freight friction, unit economics, and machine learning into ONE authoritative commercial verdict: **ENTER**, **TEST**, **WATCH**, or **AVOID**.""",
            "content_ar": """**القرار الأساسي**: *"هل يجب أن أطرح هذا المنتج في هذا السوق؟"*
تقوم المنصة بإلغاء الفوضى البصرية ودمج بيانات المبيعات التاريخية وتكاليف الشحن واقتصاديات الوحدة والتعلم الآلي لتقديم قرار تجاري موثوق ومباشر: **دخول السوق**، **اختبار تجريبي**، **مراقبة السوق**، أو **تجنب الدخول**."""
        },
        {
            "id": "2",
            "title_en": "2. Static Mode vs. Dynamic Mode",
            "title_ar": "2. الوضع الثابت مقابل الوضع التفاعلي",
            "content_en": """* **Static Mode**: Precomputed executive intelligence across 3 global datasets and 48,548 catalog products. Requires **zero initial user input** and provides instant market rankings and 20 major strategic insights.
* **Dynamic Mode**: Deep-dive interactive evaluation allowing the user to select specific products, simulate custom price points, and evaluate capital runway.""",
            "content_ar": """* **الوضع الثابت (Static)**: ذكاء سوق تنفيذي محسوب مسبقاً عبر 3 مجموعات بيانات و48,548 منتجاً. لا يتطلب أي إدخال مسبق ويعرض تصنيف الأسواق و20 رؤية فوراً.
* **الوضع التفاعلي (Dynamic)**: تحليل مخصص ومتعمق يتيح للمستخدم اختيار منتج بعينه، ومحاكاة أسعار مختلفة، وتقييم كفاية رأس المال المتاح."""
        },
        {
            "id": "3",
            "title_en": "3. Smart Product Search (Partial Matching)",
            "title_ar": "3. البحث الذكي عن المنتجات (المطابقة الجزئية)",
            "content_en": """The Smart Search bar supports multi-word, case-insensitive partial matching and keyword ranking (typing `"clock"` instantly ranks Alarm Clock, Wall Clock, and Digital Clock), displaying historical order volume and SKUs.""",
            "content_ar": """يوفر شريط البحث الذكي مطابقة جزئية وتصنيفاً ذكياً حسب الكلمات المفتاحية (كتابة `"clock"` تُظهر فوراً ساعات المنبه والحائط)، مع عرض حجم الطلبات التاريخية والرموز التعريفية."""
        },
        {
            "id": "4",
            "title_en": "4. Selecting Market & City-Level Pricing",
            "title_ar": "4. اختيار السوق والتسعير على مستوى المدينة",
            "content_en": """National benchmarks are available across United States, Brazil, United Kingdom, European Union, and Latin America. When selecting metropolitan hubs (e.g., New York, London, São Paulo), localized freight and purchasing-power multipliers adjust the recommended price corridor automatically.""",
            "content_ar": """تتوفر مؤشرات وطنية تشمل الولايات المتحدة، البرازيل، بريطانيا، الاتحاد الأوروبي، وأمريكا اللاتينية. وعند اختيار مدن كبرى (مثل نيويورك، لندن، ساو باولو)، يقوم المحرك بتطبيق مضاعفات الشحن والقدرة الشرائية لضبط السعر محلياً."""
        },
        {
            "id": "5",
            "title_en": "5. Price Intelligence & Sensitivity Slider",
            "title_ar": "5. ذكاء التسعير وشريط حساسية الطلب",
            "content_en": """The recommended price band ($X – $Y) is derived from category distributions. The interactive slider tests prices between 60% and 150% of center price, with a 7-point sensitivity curve showing how estimated success probability shifts across price points.""",
            "content_ar": """يُشتق نطاق السعر المقترح ($X – $Y) من بيانات الفئة. ويتيح شريط المحاكاة اختبار أسعار بين 60% و150% من السعر الأساسي، مع منحنى حساسية يوضح تغير احتمالية النجاح عبر 7 نقاط سعرية."""
        },
        {
            "id": "6",
            "title_en": "6. Success Probability: Estimate vs. Guarantee",
            "title_ar": "6. احتمالية النجاح: تقدير وليست ضماناً",
            "content_en": """A success probability of 78% is an **empirical estimate** produced by an isotonic-calibrated Random Forest model. It is **NOT** a guarantee of commercial success, but reflects historical likelihood under similar market and logistics parameters.""",
            "content_ar": """نسبة النجاح (مثل 78%) هي **تقدير احتمالي إحصائي** من نموذج غابات عشوائية معاير رياضياً. هي **ليست** ضماناً تجارياً، بل تعكس الاحتمال الإحصائي بناءً على تشابه المنتج مع مبيعات سابقة."""
        },
        {
            "id": "7",
            "title_en": "7. Decision Verdicts (ENTER, TEST, WATCH, AVOID)",
            "title_ar": "7. أحكام وقرارات الدخول التجارية الأربعة",
            "content_en": """* **ENTER**: Opportunity >= 75/100, Success Prob >= 65%, Low/Moderate risk.
* **TEST**: Opportunity >= 55/100, validate with pilot batch (100 units).
* **WATCH**: Opportunity 40-54/100, monitor category trends before committing capital.
* **AVOID**: Opportunity < 40/100, high freight friction (>25%), or negative unit margins.""",
            "content_ar": """* **دخول السوق (ENTER)**: فرصة >= 75/100، احتمالية نجاح >= 65%، مخاطر منخفضة/متوسطة.
* **اختبار تجريبي (TEST)**: فرصة >= 55/100، اختبار السوق بدفعة مصغرة (100 وحدة).
* **مراقبة السوق (WATCH)**: فرصة 40-54/100، مراقبة اتجاهات الفئة قبل الاستثمار.
* **تجنب الدخول (AVOID)**: فرصة < 40/100، شحن مرتفع (>25%)، أو هوامش سالبة."""
        },
        {
            "id": "8",
            "title_en": "8. Plan My Entry: Budget & Break-Even Timeline",
            "title_ar": "8. تخطيط الدخول: الميزانية وأفق نقطة التعادل",
            "content_en": """The platform computes minimum pilot capital (100 units + freight & marketing reserves) and determines whether your budget is Capital Feasible or Capital Constrained, estimating the break-even timeline (e.g. 3-5 Months).""",
            "content_ar": """تحسب المنصة الحد الأدنى لرأس مال الدفعة التجريبية وتحدد ما إذا كانت الميزانية كافية أو مقيدة، مع تقدير أفق نقطة التعادل الزمني (مثلاً 3 إلى 5 أشهر)."""
        },
        {
            "id": "9",
            "title_en": "9. Data Hierarchy: Fact vs. Estimate vs. Assumption",
            "title_ar": "9. هرمية البيانات: الحقائق والتقديرات والافتراضات",
            "content_en": """* **Historical Fact**: Audited order counts, native prices, and delivery days.
* **Model Estimate**: Calibrated Random Forest success probabilities and break-even timelines.
* **User Assumption**: Custom unit procurement costs, override target prices, and capital budgets entered by you.""",
            "content_ar": """* **الحقائق التاريخية**: أرقام الطلبات الفعلية، وأسعار المعاملات المدققة، وأيام التوصيل.
* **تقديرات النماذج**: احتمالية النجاح المحسوبة بالتعلم الآلي وأفق التعادل.
* **افتراضات المستخدم**: تكلفة التوريد المخصصة، أو السعر المستهدف، أو رأس المال المدخل من قِبلك."""
        },
        {
            "id": "10",
            "title_en": "10. Analytical Limitations & Governance",
            "title_ar": "10. القيود التحليلية وحوكمة البيانات",
            "content_en": """Models reflect observed trade patterns and cannot forecast sudden macroeconomic or geopolitical shocks. Zero synthetic fallbacks are used: missing data is never fabricated.""",
            "content_ar": """تعكس النماذج الأنماط التجارية التاريخية ولا تتنبأ بالصدمات الجيوسياسية المفاجئة. ولا يتم تزييف أو اختلاق أي بيانات مفقودة."""
        }
    ]

    topic_titles = [t["title_ar"] if is_ar else t["title_en"] for t in topics]
    sel_idx = st.selectbox(
        "اختر الموضوع للتوضيح الشامل" if is_ar else "Select Topic for Detailed Walkthrough",
        options=range(len(topics)),
        format_func=lambda i: topic_titles[i],
        key="guide_topic_select"
    )

    chosen = topics[sel_idx]

    # Render Content without repeating the title (Section 208)
    chosen_content = chosen['content_ar'] if is_ar else chosen['content_en']
    st.markdown(f"""<div style="background:#ffffff;border:1px solid #e2e8f0;border-left:4px solid #0f172a;border-radius:6px;padding:12px 16px;margin-top:8px;margin-bottom:12px;box-shadow:0 1px 3px rgba(0,0,0,0.05);">
<div style="font-size:0.90rem;line-height:1.55;color:#334155;">{chosen_content}</div>
</div>""", unsafe_allow_html=True)

    # 4 Quick Step Cards (Flush-left)
    st.caption("سير العمل السريع (4 خطوات)" if is_ar else "Quick-Start Workflow (4 Steps)")
    w1, w2, w3, w4 = st.columns(4)
    with w1:
        st.markdown(f"""<div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:8px;font-size:0.80rem;">
<strong>1. {'البحث' if is_ar else 'SEARCH'}</strong><br/>{'ابحث بالاسم أو الرمز' if is_ar else 'Type keyword or SKU'}
</div>""", unsafe_allow_html=True)
    with w2:
        st.markdown(f"""<div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:8px;font-size:0.80rem;">
<strong>2. {'السوق' if is_ar else 'MARKET'}</strong><br/>{'اختر السوق والمدينة' if is_ar else 'Select market & city'}
</div>""", unsafe_allow_html=True)
    with w3:
        st.markdown(f"""<div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:8px;font-size:0.80rem;">
<strong>3. {'الميزانية' if is_ar else 'BUDGET'}</strong><br/>{'حدد رأس المال المتاح' if is_ar else 'Input capital budget'}
</div>""", unsafe_allow_html=True)
    with w4:
        st.markdown(f"""<div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:6px;padding:8px;font-size:0.80rem;">
<strong>4. {'القرار' if is_ar else 'DECIDE'}</strong><br/>{'افحص القرار والمبررات' if is_ar else 'Inspect decision card'}
</div>""", unsafe_allow_html=True)

    st.markdown("---")
    if st.button(t("btn_back_to_decide", cur_lang), type="primary", key="guide_back_btn"):
        set_app_state_val("active_screen", "DECIDE")
        st.rerun()