pipeline {
    agent any
 
    environment {
        IMAGE_NAME = "my-docker-app:v1"
        CONTAINER_NAME = "myapp"
        PORT = "8090"
    }
 
    stages {
 
        stage('Build Docker Image') {
            steps {
                sh '''
                    set -e
                    docker build -t $IMAGE_NAME .
                '''
            }
        }
 
        stage('Stop & Remove Old Container') {
            steps {
                sh '''
                    docker ps -a --format '{{.Names}}' | grep -w $CONTAINER_NAME >/dev/null 2>&1 && \
                    (docker stop $CONTAINER_NAME || true; docker rm $CONTAINER_NAME || true) || \
                    echo "No existing container"
                '''
            }
        }
 
        stage('Run Docker Container') {
            steps {
                sh '''
                    docker run -d -p $PORT:80 --name $CONTAINER_NAME $IMAGE_NAME
                '''
            }
        }
 
        stage('Wait for App') {
            steps {
                sh '''
                    for i in {1..20}; do
                        curl -sSf http://localhost:$PORT >/dev/null && exit 0
                        echo "Waiting for app to become ready..."
                        sleep 2
                    done
                    echo "App did not start"
                    exit 1
                '''
            }
        }
    }
 
    post {
        success {
            echo '✅ Deployment SUCCESS'
        }
        failure {
            echo '❌ Deployment FAILED'
        }
    }
}