import streamlit as st
import graphviz

st.title("SERVICE MANAGEMENT")
tab1, tab2, tab3, = st.tabs(["KEY CONCEPTS", "LIFECYCLES", "DATA PLANE"])

with tab1:
  st.header("SERVICE")
  st.markdown("- Abstracts a collection of tasks")
  st.markdown("- Defines desired state of tasks")
  st.markdown("- Defines desired state of tasks")
  st.markdown("- Self healing")
  
  st.header("TASK")
  st.markdown("- A unit of work assigned to a node")
  st.markdown("- One task abstracts exactly one container")
  st.markdown("- Defines desired state of tasks")
  st.markdown("- Atomic scheduling unit of Swarm")
  service_mnmgt = "https://docs.docker.com/engine/swarm/images/service-lifecycle.png"
  st.image(service_mnmgt, caption='Swarm mode accepts service, create requests and schedules tasks to worker nodes.')

with tab2:
  st.header("TASK LIFECYCLE")
  graph = graphviz.Digraph()
  graph.edge('NEW', 'PENDING')
  graph.edge('PENDING', 'ASSIGNED')
  graph.edge('ASSIGNED', 'ACCEPTED')
  graph.edge('ASSIGNED', 'REJECTED')
  graph.edge('ACCEPTED', 'PREPARING')
  graph.edge('PREPARING', 'STARTING')
  graph.edge('STARTING', 'RUNNING')
  graph.edge('RUNNING', 'ORPHANED')
  graph.edge('RUNNING', 'COMPLETE')
  graph.edge('RUNNING', 'FAILED')
  graph.edge('RUNNING', 'SHUTDOWN')
  st.graphviz_chart(graph)
  
  st.header("SERVICE & OUTSIDE WORLD")
  st.markdown("Two types of service deployment:")
  st.markdown("- Replicated: deploy a number of identical tasks will be run")
  st.markdown("- Global: a service that runs one task on every node (monitoring agents, anti-virus scanners,etc...)")
  serviceandoutsideworld = "https://docs.docker.com/engine/swarm/images/replicated-vs-global.png"
  st.image(serviceandoutsideworld, caption='Three-service replica in yellow and a global service in gray')
 
with tab3:
  st.header("THE ROUTING MESH")
  st.markdown("- Enables each node in the swarm to accept connections on published ports for any service running in the swarm")
  st.markdown("- Routes all incoming requests to published ports on available nodes to an active container.")
  routingmesh = "https://docs.docker.com/engine/swarm/images/ingress-routing-mesh.png"
  st.image(routingmesh, caption='When you access port 8080 on any node, Docker routes your request to an active container.')
  
  
