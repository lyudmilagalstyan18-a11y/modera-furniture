import streamlit as st
import base64
import html
from pathlib import Path
from datetime import date, timedelta

BASE_DIR = Path(__file__).resolve().parent
LOGO_PNG = BASE_DIR / "images" / "logo.png"

st.set_page_config(
    page_title="Modera Furniture",
    page_icon=str(LOGO_PNG),
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 1. ԴԻԶԱՅՆ ԵՎ ԳՈՒՅՆԵՐ
def add_custom_design(image_file):
    try:
        with open(image_file, "rb") as f:
            encoded_string = base64.b64encode(f.read())
        bg_data = f"data:image/jpeg;base64,{encoded_string.decode()}"
    except:
        bg_data = ""

    st.markdown(f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(245, 245, 220, 0.95), rgba(245, 245, 220, 0.95)), url("{bg_data}");
        background-attachment: fixed;
        background-size: cover;
    }}
    .main .block-container {{
        max-width: 1300px;
        width: min(1300px, calc(100vw - 2rem));
        background-color: rgba(255, 255, 255, 0.98);
        padding: 1rem 1rem 10rem;
        border-radius: 25px;
        margin: 0 auto;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }}
    .st-emotion-cache-zy6yx3 {{
        padding: 1rem 1rem 10rem !important;
    }}
    #MainMenu {{
        visibility: hidden;
    }}
    footer {{
        visibility: hidden;
    }}
    header {{
        visibility: hidden;
    }}
    [data-testid="stToolbar"] {{
        visibility: hidden;
        height: 0;
        min-height: 0;
    }}
    .site-header {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        padding: 0.2rem 0 1.2rem;
        border-bottom: 1px solid rgba(93, 64, 55, 0.15);
        margin-bottom: 2rem;
    }}
    .brand-lockup {{
        display: flex;
        align-items: center;
        gap: 0.9rem;
    }}
    .brand-name {{
        font-size: 1.9rem;
        font-weight: 700;
        letter-spacing: 0.02em;
        color: #5d4037;
    }}
    .basket-link {{
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.7rem 1rem;
        border: 1px solid rgba(93, 64, 55, 0.18);
        border-radius: 999px;
        color: #5d4037 !important;
        text-decoration: none;
        background: rgba(255, 255, 255, 0.8);
        font-weight: 600;
    }}
    .hero-wrap {{
        display: grid;
        grid-template-columns: 1.1fr 0.9fr;
        gap: 2rem;
        align-items: center;
        margin-bottom: 3rem;
    }}
    .hero-kicker {{
        text-transform: uppercase;
        letter-spacing: 0.18em;
        font-size: 0.72rem;
        color: rgba(93, 64, 55, 0.75);
        margin-bottom: 0.75rem;
    }}
    .hero-title {{
        font-size: 4rem;
        line-height: 0.95;
        margin: 0 0 1rem 0;
        font-weight: 700;
        color: #3f2d28 !important;
    }}
    .hero-copy {{
        max-width: 36rem;
        font-size: 1.05rem;
        line-height: 1.75;
        color: rgba(93, 64, 55, 0.9) !important;
        margin-bottom: 1.4rem;
    }}
    .hero-cta {{
        display: inline-block;
        padding: 0.9rem 1.5rem;
        border-radius: 999px;
        background: #8d4b52;
        color: white !important;
        text-decoration: none;
        font-weight: 600;
    }}
    .section-title {{
        font-size: 1.8rem;
        margin: 2.5rem 0 1rem;
        color: #3f2d28 !important;
    }}
    .category-title {{
        font-size: 1.2rem;
        margin: 1.5rem 0 0.5rem;
        color: #5d4037 !important;
    }}
    .subsection-title {{
        font-size: 1rem;
        margin: 1rem 0 0.6rem;
        color: rgba(93, 64, 55, 0.85) !important;
    }}
    h1, h2, h3, p, label {{
        color: #5d4037 !important;
    }}
    </style>
    """, unsafe_allow_html=True)

add_custom_design(str(LOGO_PNG))

# --- ՏԵՍԱԿԱՆԻ ԿԱՏԱԼՈԳ ---
catalog = {
    "Մանկական կահույք": {
        "Օրորոցներ": [],
        "Կոմոդներ": [],
        "Պահարաններ": ["paharan.jpg", "paharan1.jpg", "paharan2.jpg"],
        "Մահճակալներ": ["mahcakal1.jpg", "mahcakal2.jpg"],
    },
    "Ննջասենյակային կահույք": {
        "Կոմոդներ": [],
        "Պահարաններ": ["paharan.jpg", "paharan1.jpg", "paharan2.jpg"],
        "Մահճակալներ": ["mahcakal1.jpg", "mahcakal2.jpg"],
        "Հարդասեղան (Զարդասեղան)": [],
    },
    "Հյուրասենյակային կահույք": {
        "Սեղաններ": [],
        "Աթոռներ": ["ator.jpg", "ator1.jpg", "ator2.jpg", "ator3.jpg", "ator4.jpg", "ator5.jpg"],
        "Բազմոցներ": ["bazmoc1.jpg", "bazmoc2.jpg"],
        "Բազկաթոռներ": [],
        "Պուֆեր": [],
        "Պահարաններ": ["paharan.jpg", "paharan1.jpg", "paharan2.jpg"],
    },
    "Խոհանոցային կահույք": {
        "Սեղաններ": [],
        "Աթոռներ": ["ator.jpg", "ator1.jpg", "ator2.jpg", "ator3.jpg", "ator4.jpg", "ator5.jpg"],
        "Հավաքածուներ": [],
    },
}

subsection_min_days = {
    "Օրորոցներ": 10,
    "Կոմոդներ": 12,
    "Պահարաններ": 18,
    "Մահճակալներ": 20,
    "Հարդասեղան (Զարդասեղան)": 14,
    "Սեղաններ": 10,
    "Աթոռներ": 7,
    "Բազմոցներ": 21,
    "Բազկաթոռներ": 14,
    "Պուֆեր": 7,
    "Հավաքածուներ": 14,
}

product_min_days = {
    "ator.jpg": 7,
    "ator1.jpg": 7,
    "ator2.jpg": 7,
    "ator3.jpg": 7,
    "ator4.jpg": 7,
    "ator5.jpg": 7,
    "bazmoc1.jpg": 21,
    "bazmoc2.jpg": 21,
    "mahcakal1.jpg": 20,
    "mahcakal2.jpg": 20,
    "paharan.jpg": 18,
    "paharan1.jpg": 18,
    "paharan2.jpg": 18,
}

def get_min_producing_days(selected_model, subsection_name):
    if selected_model == "Իմ սեփական տարբերակը (նկարով)":
        return 21

    if selected_model in product_min_days:
        return product_min_days[selected_model]

    return subsection_min_days.get(subsection_name, 14)

if "basket" not in st.session_state:
    st.session_state.basket = []

if "basket_counter" not in st.session_state:
    st.session_state.basket_counter = 0


def format_basket_item(item):
    extra_parts = []
    if item.get("uploaded_file"):
        extra_parts.append(f"Նկար: {item['uploaded_file']}")
    if item.get("custom_note"):
        extra_parts.append(f"Նշում: {item['custom_note']}")

    return (
        f"{item['category']} / {item['subsection']} / {item['model']}"
        f" | Քանակ: {item.get('qty', 1)}"
        f" | Արտադրության նվազագույն օրեր: {item['min_days']}"
        + (f" | {' | '.join(extra_parts)}" if extra_parts else "")
    )


def basket_summary_lines():
    lines = []
    for index, item in enumerate(st.session_state.basket, start=1):
        lines.append(f"{index}. {format_basket_item(item)}")
    return lines


def basket_min_days():
    if not st.session_state.basket:
        return 0

    return max(item["min_days"] for item in st.session_state.basket)


def basket_total_items():
    return sum(item.get("qty", 1) for item in st.session_state.basket)


def basket_item_matches(item, candidate):
    return (
        item["category"] == candidate["category"]
        and item["subsection"] == candidate["subsection"]
        and item["model"] == candidate["model"]
        and item.get("uploaded_file", "") == candidate.get("uploaded_file", "")
        and item.get("custom_note", "") == candidate.get("custom_note", "")
    )


def add_item_to_basket(new_item):
    for item in st.session_state.basket:
        if basket_item_matches(item, new_item):
            item["qty"] = item.get("qty", 1) + 1
            return

    st.session_state.basket_counter += 1
    new_item["id"] = st.session_state.basket_counter
    new_item["qty"] = 1
    st.session_state.basket.append(new_item)


def add_catalog_item(category_name, subsection_name, img_name):
    product_name = img_name.split(".")[0]
    add_item_to_basket(
        {
            "category": category_name,
            "subsection": subsection_name,
            "model": product_name,
            "order_date": "",
            "min_days": get_min_producing_days(product_name, subsection_name),
            "uploaded_file": "",
            "custom_note": "",
            "delivery_note": "",
        }
    )


def add_custom_order(custom_image, custom_note, delivery_note):
    add_item_to_basket(
        {
            "category": "Անհատական պատվեր",
            "subsection": "Նկարով",
            "model": "Անհատական պատվեր",
            "order_date": "",
            "min_days": 21,
            "uploaded_file": custom_image.name if custom_image else "",
            "custom_note": custom_note.strip(),
            "delivery_note": delivery_note.strip(),
        }
    )


def render_product_cards(category_name, subsection_name, image_list):
    if not image_list:
        st.info("Այս ենթաբաժնի համար նկարներ դեռ ավելացված չեն։")
        return

    cols = st.columns(3)
    for index, img_name in enumerate(image_list):
        with cols[index % 3]:
            try:
                st.image(f"images/{img_name}", use_container_width=True)
                st.caption(f"Մոդել: {img_name.split('.')[0]}")
                if st.button("➕ Ավելացնել", key=f"add_{category_name}_{subsection_name}_{img_name}", use_container_width=True):
                    add_catalog_item(category_name, subsection_name, img_name)
                    st.success(f"{img_name.split('.')[0]} ավելացվեց զամբյուղում։")
            except:
                st.caption("Նկարը չկա")


basket_count = basket_total_items()

st.markdown('<a id="top"></a>', unsafe_allow_html=True)
header_cols = st.columns([1.1, 4, 1], vertical_alignment="center")
with header_cols[0]:
    st.image(str(LOGO_PNG), width=82)
with header_cols[2]:
    st.markdown(
        f"<a class='basket-link' href='#checkout'>🧺 Զամբյուղ <strong>{basket_count}</strong></a>",
        unsafe_allow_html=True,
    )

hero_left, hero_right = st.columns([1.05, 0.95], gap="large", vertical_alignment="center")
with hero_left:
    st.markdown("<div class='hero-kicker'>Մեր մասին</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-title'>Modera Furniture</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='hero-copy'>
        <strong>Modera Furniture-ը մասնագիտացված է բարձրակարգ կահույքի նախագծման և արտադրության մեջ։</strong>
        Մենք համադրում ենք ժամանակակից դիզայնը և ֆունկցիոնալ լուծումները՝ ստեղծելով հարմարավետ և ոճային միջավայր յուրաքանչյուրի համար։
        <br><br>
        Առաջարկում ենք անհատական մոտեցում յուրաքանչյուր հաճախորդին՝ հաշվի առնելով ձեր ճաշակը և պահանջները։ Դուք կարող եք ընտրել մեր առաջարկվող տեսականուց կամ ներկայացնել ձեր նախընտրած տարբերակը, և մենք սիրով կկյանքացնենք այն։
        <br><br>
        Մեր արտադրանքը հայկական է՝ պատրաստված բարձր որակի նյութերով և հիմնված է 20 տարվա փորձի և երաշխավորված որակի վրա։
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<a class='hero-cta' href='#products'>Տես տեսականին</a>", unsafe_allow_html=True)
with hero_right:
    st.image("images/bazmoc1.jpg", use_container_width=True)

st.markdown('<a id="custom-order"></a>', unsafe_allow_html=True)
st.markdown("<div class='section-title'>Անհատական պատվեր</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='hero-copy'>Եթե ուզում եք պատվիրել ըստ ձեր սեփական գաղափարի, կարող եք այստեղ կցել նկարն ու գրել ձեր ցանկությունը։ Մենք դա կավելացնենք զամբյուղին որպես անհատական պատվեր։</div>",
    unsafe_allow_html=True,
)
custom_image = st.file_uploader(
    "Կցեք ձեր նկարը այստեղ",
    type=["jpg", "jpeg", "png"],
    key="custom_order_upload",
)
custom_note = st.text_area(
    "Ինչպիսի՞ պատվեր եք ցանկանում",
    placeholder="Գրեք չափերը, գույնը, նյութը կամ ցանկացած այլ մանրամասներ...",
    key="custom_order_note",
)

if custom_image:
    st.image(custom_image, use_container_width=True)

custom_order_button = st.button("➕ Ավելացնել անհատական պատվերը զամբյուղում", use_container_width=True)
if custom_order_button:
    if not custom_image:
        st.warning("Խնդրում ենք կցել նկար, որպեսզի կարողանանք ավելացնել անհատական պատվերը։")
    else:
        add_custom_order(custom_image, custom_note, "")
        st.success("Անհատական պատվերը ավելացվեց զամբյուղում։")

st.markdown('<a id="products"></a>', unsafe_allow_html=True)
st.markdown("<div class='section-title'>Տեսականի</div>", unsafe_allow_html=True)

for category_name, subsections in catalog.items():
    with st.expander(category_name, expanded=False):
        for subsection_name, image_list in subsections.items():
            with st.expander(subsection_name, expanded=False):
                render_product_cards(category_name, subsection_name, image_list)

st.markdown('<a id="checkout"></a>', unsafe_allow_html=True)
st.markdown("<div class='section-title'>Զամբյուղ</div>", unsafe_allow_html=True)

if st.session_state.basket:
    for item in st.session_state.basket:
        item_cols = st.columns([7, 1, 1, 1, 1])
        with item_cols[0]:
            st.write(format_basket_item(item))
        with item_cols[1]:
            if st.button("➖", key=f"minus_{item['id']}", use_container_width=True):
                if item.get("qty", 1) > 1:
                    item["qty"] = item.get("qty", 1) - 1
                else:
                    st.session_state.basket = [
                        basket_item for basket_item in st.session_state.basket
                        if basket_item["id"] != item["id"]
                    ]
                st.rerun()
        with item_cols[2]:
            st.markdown(f"<div style='text-align:center; font-weight:700; padding-top:0.5rem;'>{item.get('qty', 1)}</div>", unsafe_allow_html=True)
        with item_cols[3]:
            if st.button("➕", key=f"plus_{item['id']}", use_container_width=True):
                item["qty"] = item.get("qty", 1) + 1
                st.rerun()
        with item_cols[4]:
            if st.button("🗑️", key=f"remove_{item['id']}", use_container_width=True):
                st.session_state.basket = [
                    basket_item for basket_item in st.session_state.basket
                    if basket_item["id"] != item["id"]
                ]
                st.rerun()

    if st.button("🧹 Մաքրել զամբյուղը", use_container_width=True):
        st.session_state.basket = []
        st.rerun()

    st.write("---")
    st.markdown("**Ընտրված պատվերների ամփոփում**")
    st.text_area(
        "Զամբյուղի պարունակությունը",
        value="\n".join(basket_summary_lines()),
        height=180,
        disabled=True,
        label_visibility="collapsed",
    )

    basket_summary_text = "\n".join(basket_summary_lines())
    min_days_for_basket = basket_min_days()
    earliest_date = date.today() + timedelta(days=min_days_for_basket)
    order_date = st.date_input(
        "Ե՞րբ եք ցանկանում ստանալ",
        min_value=earliest_date,
        value=earliest_date,
    )
    st.caption(
        f"Զամբյուղի համար ամենավաղ հնարավոր օրը՝ {earliest_date.strftime('%Y-%m-%d')} "
        f"({min_days_for_basket} օր արտադրության ժամանակ)"
    )

    contact_form = f"""
    <form action="https://formsubmit.co/lyudmilagalstyan.18@gmail.com" method="POST">
        <input type="hidden" name="Date" value="{order_date}">
        <textarea name="Order" style="display:none;">{html.escape(basket_summary_text)}</textarea>
        <input type="text" name="name" placeholder="Ձեր անունը" style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;" required>
        <input type="text" name="phone" placeholder="Հեռախոսահամար" style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;" required>
        <input type="email" name="email" placeholder="Ձեր էլ. հասցեն" style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;" required>
        <textarea name="message" placeholder="Լրացուցիչ նշումներ..." style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; height: 100px;"></textarea>
        <button type="submit" style="background-color: #5d4037; color: white; padding: 12px; border: none; border-radius: 10px; width: 100%; cursor: pointer; font-weight: bold; font-size: 1.1em;">Ուղարկել բոլոր պատվերները</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)
else:
    st.info("Ավելացրեք ապրանքներ զամբյուղում, որպեսզի կարողանաք ուղարկել պատվերը։")
