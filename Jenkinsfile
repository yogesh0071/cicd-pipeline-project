pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/yogesh0071/cicd-pipeline-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t yogesh-app:latest .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop yogesh-app || true'
                sh 'docker rm yogesh-app || true'
            }
        }

        stage('Deploy New Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name yogesh-app yogesh-app:latest'
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}