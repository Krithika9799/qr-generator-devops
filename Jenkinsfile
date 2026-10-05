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
                bat 'docker --version'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t qr-generator:latest .'
            }
        }
        stage('Test') {
            steps {
                echo 'Running Application Tests'
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