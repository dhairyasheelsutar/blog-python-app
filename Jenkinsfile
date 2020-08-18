pipeline {
    agent any

    environment {
        WORKSPACE = "/home/ubuntu"
        OTHER_INSTANCE_IP = "172.31.45.6"
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
                    scp -r ${WORKSPACE}/blog-python-app/* 172.31.45.6:${WORKSPACE}/blog-python-app/
                    ssh 172.31.45.6
                    sudo virtualenv ${WORKSPACE}/envs/venv --python=python3
                    . ${WORKSPACE}/envs/venv/bin/activate
                    cd ${WORKSPACE}/blog-python-app
                    sudo pip3 install -r requirements.txt
                    python3 app.py
                """
            }
        }
    }
}