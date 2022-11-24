import streamlit as st

st.title("Demo")

tab1, tab2, tab3 = st.tabs(["TOPOLOGY", "SCENARIOS" ,"LINKS"])

with tab1:
  st.header("TOPOLOGY")
  st.markdown("- Abstracts a collection of tasks")
  
  from PIL import Image
  topo1 = Image.open('/app/pages/topo1.png')
  st.image(topo1)

  topo2 = Image.open('/app/pages/topo2.png')
  st.image(topo2)
  
with tab2:
  st.header("SCENARIOS")
  st.markdown("1/ SWARMS & SERVICES")
  st.markdown("- Creating a Swarm")
  st.markdown("- Starting a Service")
  st.markdown("- Node Failure Recovery")
  st.markdown("2/ LOAD BALANCING & THE ROUTING MESH")
  st.markdown("- Observe load balancing and Scale")
  st.markdown("- The Routing Mesh")
  st.markdown("- Cleanup")
  st.markdown("3/ APPLICATION DEPLOYMENT")
  st.markdown("- Dockercoin on Swarm")
  st.markdown("- Scaling and Scheduling Services")
  st.markdown("- Updating a Service")
with tab3:
  st.header("LINKS")
  import streamlit as st 
  st.write("[Swarmpit link](http://docker.demo.ai/swarmpit)")
  st.write("[Jenkins link](http://jenkins.docker.demo.ai/)")
