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

# --- ՄԵՐ ՄԱՍԻՆ ---
st.header("✨ Մեր մասին")
st.markdown("<p style='font-size: 1.1em;'>Modera Furniture-ը մասնագիտացված է բարձրակարգ կահույքի նախագծման և արտադրության մեջ։</p>", unsafe_allow_html=True)
st.write("---")

# --- ՏԵՍԱԿԱՆԻ ---
st.header("🛋️ Մեր Տեսականին")
category = st.selectbox("Ընտրեք բաժինը", ["--- Ընտրել բաժինը ---", "Աթոռներ", "Բազմոցներ", "Մահճակալներ", "Պահարաններ"])

all_models = ["--- Ընտրեք մոդելը ---", "Իմ սեփական տարբերակը (նկարով)"]
if category == "Աթոռներ":
    all_models += ["ator", "ator1", "ator2", "ator3", "ator4", "ator5"]
elif category == "Բազմոցներ":
    all_models += ["bazmoc1", "bazmoc2"]
elif category == "Մահճակալներ":
    all_models += ["mahcakal1", "mahcakal2"]
elif category == "Պահարաններ":
    all_models += ["paharan", "paharan1", "paharan2"]

def display_images(image_list):
    cols = st.columns(3)
    for index, img_name in enumerate(image_list):
        with cols[index % 3]:
            try:
                st.image(f"images/{img_name}", use_container_width=True)
                st.caption(f"Մոդել: {img_name.split('.')[0]}")
            except:
                st.caption("Նկարը չկա")

if category != "--- Ընտրել բաժինը ---":
    display_images([img for img in all_models if img not in ["--- Ընտրեք մոդելը ---", "Իմ սեփական տարբերակը (նկարով)"]])

st.write("---")

# --- ՊԱՏՎԵՐԻ ԲԱԺԻՆ ---
st.header("📅 Պատվիրել")

# 1. Մոդելի և Ամսաթվի ընտրություն
col_order1, col_order2 = st.columns(2)
with col_order1:
    selected_model = st.selectbox("Ո՞ր մոդելն եք ընտրել", all_models)
with col_order2:
    order_date = st.date_input("Ե՞րբ եք ցանկանում ստանալ", min_value=date.today())

# 2. Սեփական նկար բեռնելու դաշտ
uploaded_file = st.file_uploader("Ունե՞ք ձեր սեփական նախագիծը (կարող եք կցել նկարը)", type=['jpg', 'png', 'jpeg'])

# 3. Պատվերի ուղարկման ֆորմա
contact_form = f"""
<form action="https://formsubmit.co/lyudmilagalstyan.18@gmail.com" method="POST">
     <input type="hidden" name="Մոդել" value="{selected_model}">
     <input type="hidden" name="Ցանկալի Ամսաթիվ" value="{order_date}">
     
     <input type="text" name="name" placeholder="Ձեր անունը" style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;" required>
     <input type="text" name="phone" placeholder="Հեռախոսահամար" style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;" required>
     <input type="email" name="email" placeholder="Ձեր էլ. հասցեն" style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;" required>
     
     <textarea name="message" placeholder="Լրացուցիչ նշումներ (եթե նկար եք բեռնել, նշեք այդ մասին)...
