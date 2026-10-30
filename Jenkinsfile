pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out QR code generator'
            }
        }
        stage('Check Docker') {
            steps {
                bat '"%DOCKER_PATH%\\docker.exe" --version'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat '"%DOCKER_PATH%\\docker.exe" build -t qr-generator:latest .'
            }
        }
        stage('Test') {
            steps {
                echo 'Running Application Tests'
            }
        }
        stage('check Kubernetes access ') {
            steps {
                bat '''
                    "C:\\Users\\admin\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\kubectl.exe" version --client
                    "C:\\Program Files\\Kubernetes\\Minikube\\minikube.exe" status 
                '''
            }
        }
    }
        post {
        success {
            echo 'QR Generator pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}