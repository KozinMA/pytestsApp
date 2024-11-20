Jenkinsfile
pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/KozinMA/pytestsApp.git'
            }
        }
        stage('Build') {
            steps {
                sh '''
                  python -m pip install --upgrade pip
                  pip install -r requirements.txt
                '''
            }
        }
        stage('Tests') {
            steps {
                sh 'pytest --junitxml=result.xml tests3.py'
            }
        }
    }
}