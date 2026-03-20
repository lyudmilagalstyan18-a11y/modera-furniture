import streamlit as st
import base64
from datetime import date

# 1. ՔՈ ՀԻՆ ԴԻԶԱՅՆԸ
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
st.markdown("<h1 style='text-align: center;'>Modera Furniture</h1>", unsafe_allow_html=True)
st.write("---")

# --- ՏԵՍԱԿԱՆԻ ԵՎ ՄՈԴԵԼՆԵՐԻ ՍԱՀՄԱՆՈՒՄ ---
st.header("🛋️ Մեր Տեսականին")
category = st.selectbox("Ընտրեք բաժինը", ["--- Ընտրել բաժինը ---", "Աթոռներ", "Բազմոցներ", "Մահճակալներ", "Պահարաններ"])

# Այստեղ սահմանում ենք մոդելները, որ սխալ չտա
all_models = ["--- Ընտրեք մոդելը ---"]
if category == "Աթոռներ":
    all_models += ["ator", "ator1", "ator2", "ator3", "ator4", "ator5"]
elif category == "Բազմոցներ":
    all_models += ["bazmoc1", "bazmoc2"]
elif category == "Մահճակալներ":
    all_models += ["mahcakal1", "mahcakal2"]
elif category == "Պահարաններ":
    all_models += ["paharan", "paharan1", "paharan2"]

# Նկարների ցուցադրում
def display_images(image_list):
    cols = st.columns(3)
    for index, img_name in enumerate(image_list):
        with cols[index % 3]:
            try:
                st.image(f"images/{img_name}", use_container_width=True)
                st.caption(f"Մոդել: {img_name.split('.')[0]}")
            except:
                st.caption("Նկարը չկա")

if category == "Աթոռներ":
    display_images(["ator.jpg", "ator1.jpg", "ator2.jpg", "ator3.jpg", "ator4.jpg", "ator5.jpg"])
elif category == "Բազմոցներ":
    display_images(["bazmoc1.jpg", "bazmoc2.jpg"])
elif category == "Մահճակալներ":
    display_images(["mahcakal1.jpg", "mahcakal2.jpg"])
elif category == "Պահարաններ":
    display_images(["paharan.jpg", "paharan1.jpg", "paharan2.jpg"])

st.write("---")

# --- ՊԱՏՎԵՐԻ ԲԱԺԻՆ ---
st.header("📅 Պատվիրել")

selected_model = st.selectbox("Ո՞ր մոդելն եք ընտրել", all_models)
order_date = st.date_input("Ե՞րբ եք ցանկանում ստանալ պատվերը", min_value=date.today())

contact_form = f"""
<form action="https://formsubmit.co/lyudmilagalstyan.18@gmail.com" method="POST">
     <input type="hidden" name="_subject" value="Նոր պատվեր Modera-ից">
     <input type="hidden" name="Մոդել" value="{selected_model}">
     <input type="hidden" name="Ամսաթիվ" value="{order_date}">
     <input type="text" name="name" placeholder="Ձեր անունը" style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;" required>
     <input type="text" name="phone" placeholder="Հեռախոսահամար" style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;" required>
     <textarea name="message" placeholder="Լրացուցիչ նշումներ..." style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; height: 80px;"></textarea>
     <button type="submit" style="background-color: #5d4037; color: white; padding: 10px; border: none; border-radius: 5px; width: 100%; cursor: pointer; font-weight: bold;">Ուղարկել պատվերը</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)
