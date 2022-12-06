pipeline {
  agent any

  stages {
    stage('Checkout: streamlit source code') {
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
          sh 'docker build -t streamlit .'
          sh 'docker run --name streamlit -p 8501:8501 -d streamlit'
        }
      }
    }
  }
}
}
