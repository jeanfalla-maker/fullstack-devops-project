#!/bin/bash
set -e

if [ ! -f .env ]; then
  echo "No existe el archivo .env. Copia .env.example a .env y edítalo."
  exit 1
fi

source .env

IMAGE_NAME="$DOCKERHUB_USERNAME/$DOCKERHUB_REPO:$IMAGE_TAG"

echo "Construyendo imagen $IMAGE_NAME ..."
docker build -t "$IMAGE_NAME" ./app

echo "Iniciando sesión en Docker Hub..."
docker login

echo "Publicando imagen en Docker Hub..."
docker push "$IMAGE_NAME"

echo "Imagen publicada correctamente: $IMAGE_NAME"
