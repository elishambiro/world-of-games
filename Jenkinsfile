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
              dir("/var/lib/jenkins/workspace/world-of-games/") {
                    sh "docker build -t elishambiro/project:v0.1 ."
              } 
          }
      }
      stage('Run'){
          steps {
                    dir("/var/lib/jenkins/workspace/world-of-games/") {
                        sh "docker-compose up"
                    }
          }
      }
      stage('Test'){
          steps {
                    dir("/var/lib/jenkins/workspace/world-of-games/") {
                        sh 'python3 /tests/e2e.py'
                    }
          }
      }
      stage('Finalize'){
          steps {
                     dir("/var/lib/jenkins/workspace/world-of-games/") {
                         sh "docker-compose down"
                     }
          }
      }
    }
 }
