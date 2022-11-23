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

dataplaneimage = "https://blog.octo.com/wp-content/uploads/2017/08/controlplane.png"
vxlanimage = "https://blog.octo.com/wp-content/uploads/2017/08/packetwalkvxlan.png"
st.header("DATA PLANE")
st.markdown("- This includes container traffic and traffic to and from external clients.")
st.image(dataplaneimage, caption='Control Plane')

st.markdown("- It uses standard VXLAN to encapsulate container traffic and send it to other containers")
st.markdown("- VXLAN is an encapsulation format that wraps Layer 2 segments with an IP/UDP header, and then send it over Layer 3 networks")
st.image(vxlanimage, caption='Networking on Control Plan')
