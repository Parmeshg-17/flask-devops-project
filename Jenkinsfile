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

        stage('Stop Old Containers') {
            steps {
                sh 'docker-compose down || true'
            }
        }

        stage('Build & Deploy') {
            steps {
                sh 'docker-compose up --build -d'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'docker ps'
            }
        }
    }
}
