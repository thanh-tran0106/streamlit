import streamlit as st

st.title("CONTROL PLANE")

st.header("SWIM PROTOCOL")
st.markdown("- Ask neighbor A if they're still alive")
st.markdown("- Ask three other neighbors if they can reach neighbor A")
st.markdown("- No to both: conclude neighbor A is unhealthy/dead")


fakeimage = "https://cdn.dribbble.com/users/1100256/screenshots/3639908/swim.gif"
st.image(fakeimage, caption='SWIM')

st.markdown("Just kidding, this is the real one ^^")

image = "https://hqt.github.io/assets/img/2020-07-07/swim_failure_detector.png"
#
st.image(image, caption='Failure Detection')

st.header("GOSSIP CONTROL PLANE")
st.markdown("- Docker control plane: piggyback DNS info on SWIM traffic")
st.markdown("- DNS entries spread 'infectiously' through cluster.")
st.markdown("- Gossip control plane scales independent of cluster size")
