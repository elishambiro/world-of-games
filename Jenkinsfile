pipeline {
  stages {
    stage('Checkout') {
      git 'https://github.com/elishambiro/world-of-games.git'
    }
    stage('Build'){ 
      bat'docker build -t elishambiro/project:v0.1 .'
      echo 'build!'
    }
    stage('Run'){
      bat 'docker-compose up'
    }
    stage('Test'){
      bat 'python3 /tests/e2e.py'
    }
    stage('Finalize'){
      bat 'docker-compose down'
      echo 'done'
    }
}
}
