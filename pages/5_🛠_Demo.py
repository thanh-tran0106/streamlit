import streamlit as st

st.title("Demo")

tab1, tab2 = st.tabs(["TOPOLOGY", "LINKS"])

with tab1:
  st.header("TOPOLOGY")
  st.markdown("- Abstracts a collection of tasks")
  
  from PIL import Image
  topo1 = Image.open('/app/pages/topo1.png')
  st.image(topo1)

  topo2 = Image.open('/app/pages/topo2.png')
  st.image(topo2)
  
with tab2:
  st.header("LINKS")
  import streamlit as st 
  st.write("[Swarmpit link](http://docker.demo.ai/swarmpit)")
  st.write("[Jenkins link](http://jenkins.docker.demo.ai/)")
