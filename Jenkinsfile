pipeline {
    agent any

    environment {
        WORKSPACE = "/home/ubuntu"
    }

    stages {
        stage('Cleanup') {
            steps {
                sh """

                    if [ -d ${WORKSPACE}/blog-python-app/ ]; then
                        sudo rm -r ${WORKSPACE}/blog-python-app/
                    fi

                    if [ -d ${WORKSPACE}/envs/ ]; then
                        sudo rm -r ${WORKSPACE}/envs/
                    fi
                   
                """
            }
        }
        stage('Checkout') {
            steps {
                sh """
                    sudo git clone https://github.com/dhairyasheelsutar/blog-python-app.git ${WORKSPACE}/blog-python-app/
                """
            }
        }
        stage('Build') {
            steps {
                sh """
                    sudo virtualenv ${WORKSPACE}/envs/venv --python=python3
                    . ${WORKSPACE}/envs/venv/bin/activate
                    cd ${WORKSPACE}/blog-python-app
                    sudo pip3 install -r requirements.txt
                """
            }
        }
        stage('Test') {
            steps {
                sh """
                    . ${WORKSPACE}/envs/venv/bin/activate
                    cd ${WORKSPACE}/blog-python-app/test
                    python3 -m unittest test_app.py
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