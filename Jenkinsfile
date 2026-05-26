pipeline {
    agent {
        label 'built-in'
    }

    stages {

        stage('System Check') {
            steps {
                sh 'echo Jenkins Pipeline Started'
                sh 'free -h'
                sh 'df -h'
            }
        }

        stage('Docker Check') {
            steps {
                sh 'docker ps'
            }
        }
    }
}
