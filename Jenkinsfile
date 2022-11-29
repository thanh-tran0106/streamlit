pipeline {
  agent{
    label "agent1"
  }

  stages {
    stage('Checkout: strealit source code') {
      steps {
        dir('streamlit') {
          git branch : 'main',
            url : 'https://github.com/thanh-tran0106/streamlit.git'
        }     
      }
    }
  
  stage('Streamlit tear down and recreate') {
    steps {
      script {
        dir('streamlit') {
          sh 'ls -la'
          sh 'docker rm -f streamlit'
          sh 'docker stack deploy -c streamlit-stack.yaml streamlit'
        }
      }
    }
  }
}
}
