pipeline {
    agent {
        label 'built-in'
    }

    stages {

        stage('System Check') {
            steps {
                sh 'free -h'
                sh 'df -h'
            }
        }

        stage('Pull Latest Code') {
            steps {
                sh 'git pull origin main || true'
            }
        }

        stage('Restart Flask Container') {
            steps {
                sh 'docker restart flaskapp'
            }
        }

        stage('Verify Containers') {
            steps {
                sh 'docker ps'
            }
        }
    }
}
