import streamlit as st
import base64

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
    .stButton>button {{
        background-color: #5d4037 !important;
        color: #ffffff !important;
        border-radius: 10px;
        border: 2px solid #8d6e63;
        width: 100%;
        font-weight: bold;
        height: 3em;
        font-size: 1.2em;
    }}
    </style>
    """, unsafe_allow_html=True)

add_custom_design('images/logo.jpg')

# --- ԼՈԳՈ ԵՎ ՎԵՐՆԱԳԻՐ ---
st.markdown("<h1 style='text-align: center;'>Modera Furniture</h1>", unsafe_allow_html=True)
st.write("---")

# --- ՄԵՐ ՄԱՍԻՆ ---
st.header("✨ Մեր մասին")
st.write("Modera Furniture-ը մասնագիտացված է բարձրակարգ կահույքի նախագծման մեջ։")
st.write("---")

# --- ՏԵՍԱԿԱՆԻ ---
st.header("🛋️ Մեր Տեսականին")
category = st.selectbox("Ընտրեք բաժինը", ["Աթոռներ", "Բազմոցներ", "Մահճակալներ", "Պահարաններ"])

def display_images(image_list):
    cols = st.columns(2)
    for index, img_name in enumerate(image_list):
        with cols[index % 2]:
            try:
                st.image(f"images/{img_name}", use_container_width=True)
            except:
                st.write("Նկարը չկա")

if category == "Աթոռներ":
    display_images(["ator.jpg", "ator1.jpg", "ator2.jpg", "ator3.jpg", "ator4.jpg", "ator5.jpg"])
elif category == "Բազմոցներ":
    display_images(["bazmoc1.jpg", "bazmoc2.jpg"])
elif category == "Մահճակալներ":
    display_images(["mahcakal1.jpg"])
elif category == "Պահարաններ":
    display_images(["paharan.jpg", "paharan1.jpg", "paharan2.jpg"])

st.write("---")

# --- ՊԱՏՎԵՐ ---
st.header("📅 Պատվիրել")

contact_form = """
<form action="https://formsubmit.co/lyudmilagalstyan.18@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Ձեր անունը" style="width: 100%; padding: 10px; margin-bottom: 10px;" required>
     <input type="email" name="email" placeholder="Ձեր էլ. հասցեն" style="width: 100%; padding: 10px; margin-bottom: 10px;" required>
     <textarea name="message" placeholder="Ինչ մոդել եք ցանկանում" style="width: 100%; padding: 10px; margin-bottom: 10px;"></textarea>
     <button type="submit" style="background-color: #5d4037; color: white; padding: 10px; border: none; border-radius: 5px; width: 100%;">Ուղարկել հայտը</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

st.write("---")
st.write("© 2026 Modera Furniture")
