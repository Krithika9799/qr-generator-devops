pipeline {
    agent any

    environment {
        DOCKER_PATH = 'C:\\Users\\admin\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin'
        KUBECONFIG = 'C:\\Users\\admin\\.kube\\config'
        IMAGE_NAME = 'qr-generator:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out QR Generator project'
            }
        }

        stage('Check Docker') {
            steps {
                bat '"%DOCKER_PATH%\\docker.exe" --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"%DOCKER_PATH%\\docker.exe" build -t %IMAGE_NAME% .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Application Tests'
            }
        }

        stage('Check Kubernetes Access') {
            steps {
                bat '''
                    "%DOCKER_PATH%\\kubectl.exe" get nodes
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat '''
                    "%DOCKER_PATH%\\docker.exe" save %IMAGE_NAME% -o qr-generator.tar

                    "C:\\Program Files\\Kubernetes\\Minikube\\minikube.exe" image load qr-generator.tar

                    "%DOCKER_PATH%\\kubectl.exe" apply -f deployment.yaml

                    "%DOCKER_PATH%\\kubectl.exe" apply -f service.yaml
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                bat '''
                    "%DOCKER_PATH%\\kubectl.exe" rollout status deployment/qr-generator --timeout=120s

                    "%DOCKER_PATH%\\kubectl.exe" get deployments

                    "%DOCKER_PATH%\\kubectl.exe" get pods

                    "%DOCKER_PATH%\\kubectl.exe" get services
                '''
            }
        }
    }

    post {
        success {
            echo 'QR Generator CI/CD pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
