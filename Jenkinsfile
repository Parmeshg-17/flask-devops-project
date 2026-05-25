pipeline {
    agent any
    stages {
        stage('Clone repo') {
            steps {
                // NOTE: Replace this URL with your actual GitHub repository URL
                git branch: 'main', url: 'https://github.com/Parmeshg-17/flask-devops-project.git'
            }
        }
        stage('Build image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }
        stage('Deploy with docker compose') {
            steps {
                // Remove existing containers if they are running
                sh 'docker compose down || true'
                // Start app, rebuilding the flask image
                sh 'docker compose up -d --build'
            }
        }
    }
}

