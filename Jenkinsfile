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
                    dir("WoG/") {
                        
                        bat "docker-compose up"
                    }
                )
          }
      }
      stage('Test'){
          steps {
                parallel(
                    dir("WoG/") {
                        bat 'python3 /tests/e2e.py'
                    }
                )
          }
      }
      stage('Finalize'){
          steps {
                parallel(
                     dir("WoG/") {
                         bat "docker-compose down"
                     }
                )
          }
      }
    }
 }
