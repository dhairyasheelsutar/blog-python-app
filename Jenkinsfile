Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any

    environment {
        WORKSPACE = "/home/ubuntu"
    }

    stages {
        stage('Cleanup') {
            steps {
                echo 'Cleanup...'
            }
        }
        stage('Checkout') {
            steps {
                sh """
                    git clone https://github.com/dhairyasheelsutar/blog-python-app.git
                """
            }
        }
        stage('Build') {
            steps {
                sh """
                    virtualenv ${WORKSPACE}/envs/venv --python=python3
                    cd ${WORKSPACE}/blog-python-app
                    pip3 install -r requirements.txt
                """
            }
        }
        stage('Test') {
            steps {
                sh """
                    source ${WORKSPACE}/envs/venv/bin/activate
                    cd ${WORKSPACE}/blog-python-app
                    python3 -m unittest test/test_app.py
                """
            }
        }
        stage('Deploy') {
            steps {
                sh """
                    cd ${WORKSPACE}/blog-python-app
                    python3 app.py
                """
            }
        }
    }
}