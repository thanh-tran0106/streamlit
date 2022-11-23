import streamlit as st

st.title("CONTROL PLANE")

st.header("SWIM PROTOCOL")
st.markdown("- Ask neighbor A if they're still alive")
st.markdown("- Ask three other neighbors if they can reach neighbor A")
st.markdown("- No to both: conclude neighbor A is unhealthy/dead")


fakeimage = "https://c.tenor.com/T4HzdRJwVQIAAAAC/swim-in.gif"
st.image(fakeimage, caption='SWIM')

st.markdown("Just kidding, this is the real one ^^")

image = "https://www.brianstorti.com/assets/images/swim/failure-detection.png"
#
st.image(image, caption='Failure Detection')
