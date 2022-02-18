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
                    bat'docker build -t elishambiro/project:v0.1 .'
                    echo 'build!'
                )
          }
      }
      stage('Run'){
          steps {
                parallel(
                    bat 'docker-compose up'
                )
          }
      }
      stage('Test'){
          steps {
                parallel(
                    bat 'python3 /tests/e2e.py'
                )
          }
      }
      stage('Finalize'){
          steps {
                parallel(
                    bat 'docker-compose down'
                    echo 'done'
                )
          }
      }
    }
 }
