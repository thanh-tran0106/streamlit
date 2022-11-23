import streamlit as st

st.title("Docker Swarm")

st.header("DISTRIBUTED APPLICATION ARCHITECTURE")
st.markdown("- Applications consisting of one or more containers across one or more nodes")
st.markdown("- Docker Swarm facilitates multi-node design.")
st.markdown("- Also supports multiple interacting services (like Compose)")

st.header("NETWORKING REQUIREMENTS")
url = " "
st.markdown("- Control plane:"  % url "enable service discovery for containers across hosts")
st.markdown("- Data plane: enable moving a packet from host A to host B")
st.markdown("- Management plane: decide where containers should be scheduled")

#open the image
image = "https://docs.docker.com/engine/swarm/images/swarm-diagram.png"
#
st.image(image, caption='Swarm Diagram')
