import streamlit as st

st.title("CONTROL PLANE")

st.header("SWIM PROTOCOL")
st.markdown("- Ask neighbor A if they're still alive")
st.markdown("- Ask three other neighbors if they can reach neighbor A")
st.markdown("- No to both: conclude neighbor A is unhealthy/dead")
