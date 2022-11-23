import streamlit as st

st.set_page_config(
    page_title="Docker Demo",
    page_icon="🌤",
)
from PIL import Image
image = Image.open('lampstring.png')

st.image(image)

st.title("Welcome to Docker Swarm Demo")
st.header("Prenseted by Thien Thanh 🌤")
st.markdown("Agenda")

xmastree = "https://www.citypng.com/photo/15778/hd-golden-sparkle-christmas-tree-png"
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



