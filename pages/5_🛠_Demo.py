import streamlit as st

st.title("Demo")


from PIL import Image
topo1 = Image.open('/app/pages/topo1.png')

st.image(topo1)

topo2 = Image.open('/app/pages/topo2.png')

st.image(topo2)
