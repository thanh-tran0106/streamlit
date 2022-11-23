import streamlit as st

st.set_page_config(
    page_title="Docker Demo",
    page_icon="🌤",
)
from PIL import Image
image = Image.open('lampstring.png')

st.image(image)


st.markdown("<h1 style='text-align: center; color: white;'>Welcome to Docker Swarm Demo</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: white;'>Prenseted by Thien Thanh 🌤</h2>", unsafe_allow_html=True)

xmastree = "xmastree.png"
st.image(xmastree)

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

# Load Animation
animation_symbol = "❄"

st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True,
)



