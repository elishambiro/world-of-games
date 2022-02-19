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
          docker { image 'elishambiro/project:v0.1' }
          stages {
              stage('Test') {
                  steps {
                      sh 'node --version'
                  }
              }
                       
                    
          }
      }
      stage('Test'){
          steps {
                    dir("/var/lib/jenkins/workspace/world-of-games/") {
                        sh 'cd tests/ && python3 e2e.py'
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
