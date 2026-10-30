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
                    set KUBECONFIG=C:\\Users\\admin\\.kube\\config

                    "C:\\Users\\admin\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\kubectl.exe" config current-context

                    "C:\\Users\\admin\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\kubectl.exe" get nodes

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