import streamlit as st

st.title("DOCKER SWARM NETWORKING")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["SWIM PROTOCOL", "GOSSIP CONTROL PLANE", "DATA PLANE", "MANAGEMENT PLANE", "RAFT CONSENSUS"])

with tab1:
  
  st.header("SWIM PROTOCOL")
  st.markdown("- Ask neighbor A if they're still alive")
  st.markdown("- Ask three other neighbors if they can reach neighbor A")
  st.markdown("- No to both: conclude neighbor A is unhealthy/dead")
  fakeimage = "https://cdn.dribbble.com/users/1100256/screenshots/3639908/swim.gif"
  st.image(fakeimage, caption='SWIM')
  st.markdown("Just kidding, this is the real one ^^")
  image = "https://hqt.github.io/assets/img/2020-07-07/swim_failure_detector.png"
  st.image(image, caption='Failure Detection')

with tab2:
  st.header("GOSSIP CONTROL PLANE")
  st.markdown("- Docker control plane: piggyback DNS info on SWIM traffic")
  st.markdown("- DNS entries spread 'infectiously' through cluster.")
  st.markdown("- Gossip control plane scales independent of cluster size")
  gossipimg = "https://hqt.github.io/assets/img/2020-07-07/swim_dissemination_component.png"
  st.image(gossipimg, caption='SWIM: C failed, A detected and multicast to other nodes')
  
with tab3:
  dataplaneimage = "https://blog.octo.com/wp-content/uploads/2017/08/controlplane.png"
  vxlanimage = "https://blog.octo.com/wp-content/uploads/2017/08/packetwalkvxlan.png"
  st.header("DATA PLANE")
  st.markdown("- This includes container traffic and traffic to and from external clients.")
  st.image(dataplaneimage, caption='Control Plane')

  st.markdown("- It uses standard VXLAN to encapsulate container traffic and send it to other containers")
  st.markdown("- VXLAN is an encapsulation format that wraps Layer 2 segments with an IP/UDP header, and then send it over Layer 3 networks")
  st.image(vxlanimage, caption='Networking on Control Plan')

with tab4:
  st.header("MANAGEMENT PLANE")
  st.markdown("- Need a manager to decide where to schedule containers (ie update system state)")
  st.markdown("- Need multiple managers for high availability")
  st.markdown("- Raft Consensus to preserve an up-to-date system state in event of leader failure")

with tab5:
  st.header("RAFT CONSENSUS (radically simplified)")
  st.markdown("- State changes can only be proposed by a unique leader")
  st.markdown("- State cannot be changed unless a majority of members agree")
  st.markdown("- A member cannot become leader unless it is in the up-to-date majority")
  st.markdown("Result: valid leader always has an (almost) up-to-date record of state.")
  st.markdown("Requirement: a majority of managers must remain alive and reachable.")
  
