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
                    sh """docker exec -i world-of-games-web-1 bash
                          apt-get -y update
                          apt-get install -y google-chrome-stable
                          apt-get install -yqq unzip curl
                          wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
                          unzip -o /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ 
                          apt-get install -y python3 python3-pip
                          pip3 install selenium
                          python3 e2e.py
                    """
               }
          }
      }
      stage('Finalize'){
          steps {
                     dir("/var/lib/jenkins/workspace/world-of-games/") {
                         sh """docker-compose down
                               docker push elishambiro/project:v0.1
                         """
                     }
          }
      }
    }
 }
