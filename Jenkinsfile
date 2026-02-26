pipeline {
  agent any

  environment {
    IMAGE_NAME = "evancraig11/devops-assignment1"
    CONTAINER_NAME = "flask-prod"
  }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Test (pytest)') {
      steps {
        sh '''
          set -e
          python3 -m venv venv
          . venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
          pytest
        '''
      }
    }

    stage('Build Docker image') {
      steps {
        sh '''
          set -e
          docker build -t ${IMAGE_NAME}:latest .
          docker tag ${IMAGE_NAME}:latest ${IMAGE_NAME}:${BUILD_NUMBER}
        '''
      }
    }

    stage('Push to Docker Hub') {
      steps {
        withCredentials([usernamePassword(
          credentialsId: 'dockerhub-creds',
          usernameVariable: 'DOCKERHUB_USER',
          passwordVariable: 'DOCKERHUB_TOKEN'
        )]) {
          sh '''
            set -e
            echo "$DOCKERHUB_TOKEN" | docker login -u "$DOCKERHUB_USER" --password-stdin
            docker push ${IMAGE_NAME}:latest
            docker push ${IMAGE_NAME}:${BUILD_NUMBER}
          '''
        }
      }
    }

    stage('Deploy to EC2 (local)') {
      steps {
        sh '''
          set -e

          echo "Pulling latest image..."
          docker pull ${IMAGE_NAME}:latest

          echo "Stopping old container (if exists)..."
          docker rm -f ${CONTAINER_NAME} 2>/dev/null || true

          echo "Starting new container on port 5000..."
          docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}:latest

          echo "Verifying locally via Nginx upstream port..."
          sleep 2
          curl -fsS http://localhost:5000 >/dev/null
          echo "Deploy OK"
        '''
      }
    }
  }

  post {
    always {
      sh 'docker logout || true'
    }
  }
}