pipeline {
    agent any
    stages {
      stage('Checkout') {
          steps {
              checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/elishambiro/world-of-games.git']]])
          }
      }
      stage('Build'){ 
          steps {
              dir("/") {
                    bat "docker build -t elishambiro/project:v0.1 -f ./Dockerfile"
              } 
          }
      }
      stage('Run'){
          steps {
                    dir("/") {
                        bat "docker-compose up"
                    }
          }
      }
      stage('Test'){
          steps {
                    dir("/") {
                        bat 'python3 /tests/e2e.py'
                    }
          }
      }
      stage('Finalize'){
          steps {
                     dir("/") {
                         bat "docker-compose down"
                     }
          }
      }
    }
 }
