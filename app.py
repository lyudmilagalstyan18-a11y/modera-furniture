import streamlit as st
import base64
from datetime import date

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
        background-color: rgba(255, 255, 255, 0.98);
        padding: 3rem;
        border-radius: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }}
    h1, h2, h3, p, label {{
        color: #5d4037 !important;
    }}
    
    /* ԿՈՃԱԿԻ ՍՊԻՏԱԿ ՏԱՌԵՐԸ */
    .stButton>button {{
        background-color: #5d4037 !important;
        color: #ffffff !important; /* ՄԱՔՈՒՐ ՍՊԻՏԱԿ ՏԵՔՍՏ */
        border-radius: 10px;
        border: 2px solid #8d6e63;
        width: 100%;
        font-weight: bold;
        height: 3em;
        font-size: 1.2em;
    }}
    .stButton>button:hover {{
        background-color: #8d6e63 !important;
        color: #ffffff !important;
    }}

    .model-label {{
        text-align: center;
        font-weight: bold;
        color: #8d6e63;
        margin-top: -10px;
        margin-bottom: 20px;
        background: #fdf5e6;
        padding: 5px;
        border-radius: 5px;
        border: 1px solid #e2d1c3;
    }}
    </style>
    """, unsafe_allow_html=True)

add_custom_design('images/logo.jpg')

# --- ԼՈԳՈ ԵՎ ՎԵՐՆԱԳԻՐ ---
col_l, col_m, col_r = st.columns([1, 1, 1])
with col_m:
    try:
        st.image("images/logo.jpg", use_container_width=True)
    except:
        st.markdown("<h3 style='text-align: center;'>MODERA</h3>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Modera Furniture</h1>", unsafe_allow_html=True)
st.write("---")

# --- ՄԵՐ ՄԱՍԻՆ (ՎԵՐԱԿԱՆԳՆՎԱԾ) ---
st.header("✨ Մեր մասին")
st.markdown("""
<p style='font-size: 1.1em;'>
<b>Modera Furniture</b>-ը մասնագիտացված է բարձրակարգ կահույքի նախագծման և արտադրության մեջ։ 
Մենք ստեղծում ենք լուծումներ, որոնք համապատասխանում են Ձեր կյանքի ռիթմին և ճաշակին։ 
Յուրաքանչյուր դետալ մշակվում է հատուկ խնամքով՝ օգտագործելով լավագույն նյութերը։
</p>
""", unsafe_allow_html=True)
st.write("---")

# --- ՏԵՍԱԿԱՆԻ ---
st.header("🛋️ Մեր Տեսականին")
category = st.selectbox(
    "Ընտրեք բաժինը",
    ["--- Ընտրել բաժինը ---", "Աթոռներ", "Բազմոցներ", "Մահճակալներ", "Պահարաններ"]
)

def display_images(image_list):
    cols = st.columns(3)
    for index, img_name in enumerate(image_list):
        with cols[index % 3]:
            try:
                st.image(f"images/{img_name}", use_container_width=True)
                m_name = img_name.split('.')[0]
                st.markdown(f"<div class='model-label'>Մոդել: {m_name}</div>", unsafe_allow_html=True)
            except:
                st.caption(f"Նկարը չկա: {img_name}")

if category == "Աթոռներ":
    display_images(["ator.jpg", "ator1.jpg", "ator2.jpg", "ator3.jpg", "ator4.jpg", "ator5.jpg"])
elif category == "Բազմոցներ":
    display_images(["bazmoc1.jpg", "bazmoc2.jpg"])
elif category == "Մահճակալներ":
    display_images(["mahcakal1.jpg", "mahcakal2.jpg"])
elif category == "Պահարաններ":
    display_images(["paharan.jpg", "paharan1.jpg", "paharan2.jpg"])

st.write("---")

# --- ՊԱՏՎԵՐԻ ՁԵՎ ---
st.header("📅 Պատվիրել")
with st.form("order_form"):
    c1, c2 = st.columns(2)
    with c1:
        u_name = st.text_input("Ձեր անունը")
        u_phone = st.text_input("Հեռախոսահամար")
        u_date = st.date_input("Նախընտրելի ժամկետ", min_value=date.today())
    with c2:
        model_ref = st.text_input("Մոդելի անվանումը (օրինակ՝ ator1)")
        u_file = st.file_uploader("Կցեք Ձեր նախընտրած նկարը", type=['jpg', 'png'])

    u_notes = st.text_area("Լրացուցիչ նշումներ (չափսեր, գույն և այլն)")

    if st.form_submit_button("Ուղարկել հայտը"):
        if u_name and u_phone:
            st.success(f"Շնորհակալություն, {u_name}: Ձեր հայտը հաջողությամբ ուղարկվեց:")
        else:
            st.error("Խնդրում ենք լրացնել անունը և հեռախոսը:")

st.write("---")
st.markdown("<p style='text-align: center; color: #8d6e63;'>© 2026 Modera Furniture Manufacturing</p>", unsafe_allow_html=True)