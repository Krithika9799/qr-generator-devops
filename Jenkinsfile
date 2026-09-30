Pipeline
{
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out QR code generator'
            }
        }
        stage('Build') {
            steps {
                echo 'Building QR Generator Application'
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