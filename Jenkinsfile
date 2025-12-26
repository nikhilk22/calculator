pipeline{
    agent any

    environment {
        IMAGE_NAME = "nikhil22qwe/calculator"
        IMAGE_TAG  = "1.0.4"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/nikhilk22/calculator.git',
                    credentialsId: 'github-creds'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                  docker build -t $IMAGE_NAME:$IMAGE_TAG .
                '''
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                      echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                      docker push $IMAGE_NAME:$IMAGE_TAG
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                  kubectl set image deployment/calculator \
                  calculator=$IMAGE_NAME:$IMAGE_TAG \
                  --namespace=$KUBE_NAMESPACE

                  kubectl rollout status deployment/calculator \
                  --namespace=$KUBE_NAMESPACE
                '''
            }
        }
    }

    post {
        failure {
            echo "❌ Deployment failed — rolling back"
            sh '''
              kubectl rollout undo deployment/calculator \
              --namespace=$KUBE_NAMESPACE
            '''
        }
    }  
}
