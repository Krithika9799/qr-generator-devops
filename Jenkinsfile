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
                    whoami
                    dir "C:\\Users\\admin\\.kube"
                    dir "C:\\Users\\admin\\.minikube\\profiles\\minikube"
                    type "C:\\Users\\admin\\.kube\\config"

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