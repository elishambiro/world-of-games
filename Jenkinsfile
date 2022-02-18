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
              dir("WoG/") {
                    bat "docker build -t elishambiro/project:v0.1 ."
              } 
          }
      }
      stage('Run'){
          steps {
                    dir("WoG/") {
                        bat "docker-compose up"
                    }
          }
      }
      stage('Test'){
          steps {
                    dir("WoG/") {
                        bat 'python3 /tests/e2e.py'
                    }
          }
      }
      stage('Finalize'){
          steps {
                     dir("WoG/") {
                         bat "docker-compose down"
                     }
          }
      }
    }
 }
