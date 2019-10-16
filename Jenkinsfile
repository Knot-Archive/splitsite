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
            steps{
                dir("{env.WORKSPACE}")
                echo '[INFO] stat deploy'
                echo '[INFO] finish deploy'
            }
        }
    }
}