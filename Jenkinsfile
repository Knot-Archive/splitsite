pipeline {
    agent any
    stages {
        stage('testing pipeline'){
              steps{
                    echo 'test1'
                    sh 'mkdir -p from-jenkins'
                    sh 'touch from-jenkins/test.txt'
              }
        }
        stage('ansible playbook'){
            steps {
                echo 'start deploy'
                sh 'http://127.0.0.1:5000/playbook_webserver_fi-ailyun'
            }
        }
    }
}