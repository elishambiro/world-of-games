pipeline {
    agent any
    stages {
      stage('Checkout') {
          steps {
                parallel(
                    checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/elishambiro/world-of-games.git']]])
                )
          }
      }
      stage('Build'){ 
          steps {
                parallel(
                    agent { dockerfile true }
                )
          }
      }
      stage('Run'){
          steps {
                parallel(
                   useCustomDockerComposeFile true
                )
          }
      }
      stage('Test'){
          steps {
                parallel(
                    sh 'python3 /tests/e2e.py'
                )
          }
      }
      stage('Finalize'){
          steps {
                parallel(
                    useCustomDockerComposeFile false
                )
          }
      }
    }
 }
