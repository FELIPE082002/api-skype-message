pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'fastapi-app'
        CONTAINER_NAME = 'fastapi-container'
        PORT = '8721'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    // Construir la imagen Docker con un tag
                    sh 'docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Detener y eliminar el contenedor anterior si existe
                    sh 'docker stop ${CONTAINER_NAME} || true'
                    sh 'docker rm ${CONTAINER_NAME} || true'

                    // Desplegar la aplicación en la máquina Docker con un nombre específico
                    sh 'docker run -d -p ${PORT}:${PORT} --name ${CONTAINER_NAME} ${DOCKER_IMAGE}:${BUILD_NUMBER}'

                    // Limpieza: eliminar imágenes antiguas
                    sh 'docker image prune -f'
                }
            }
        }
    }

    post {
        always {
            // Notificar el resultado del despliegue
            echo 'Notificación de estado del despliegue'
        }
    }
}
