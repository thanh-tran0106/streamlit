pipeline {
  agent{
    label "agent0"
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
        }
      }
    }
  }
}
}
