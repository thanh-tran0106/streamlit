import streamlit as st

st.title("Demo")


from PIL import Image
topo1 = Image.open('topo1.png')

st.image(top1)

topo2 = Image.open('topo2.png')

st.image(top2)
