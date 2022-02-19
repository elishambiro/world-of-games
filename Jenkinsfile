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
                    sh "docker-compose up -d"
              } 
          }
      }
      stage('Test'){
        steps {
              dir("/var/lib/jenkins/workspace/world-of-games/") {
                  sh 'docker exec -i world-of-games-web-1 sh'
                  sh 'cd ~/tests'
                  sh 'python3 e2e.py'
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
