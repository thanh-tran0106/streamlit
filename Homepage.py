import streamlit as st

"""
# Welcome to my Docker Swarm Demo!

If you have any questions, checkout our [my code](https://github.com/thanh-tran0106/streamlit).

In the meantime, sit back and enjoy the demo :) 
"""

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

st.set_page_config(
    page_title="Docker Demo",
    page_icon="🌤",
)
st.title("Welcome Page")
st.sidebar.success("Select a page above")
    
