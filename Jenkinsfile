pipeline {
  stages {
    stage('Checkout') {
        git 'https://github.com/elishambiro/world-of-games.git'
    }
    stage('Build'){
        agent { dockerfile true }
        echo 'build!'
        
    }
    stage('Run'){
        useCustomDockerComposeFile true
    }
    stage('Test'){
        script{
            python3 /tests/e2e.py
        }
        }
    }
    stage('Finalize'){
        if (results == -1){
            echo "success"
            useCustomDockerComposeFile false
        }
        
    }
    }
  }
}
