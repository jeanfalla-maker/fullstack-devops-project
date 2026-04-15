#!/bin/bash
set -e

if ! command -v kubectl &> /dev/null; then
  echo "kubectl no está instalado"
  exit 1
fi

echo "Aplicando recursos en Kubernetes..."
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/db-deployment.yaml
kubectl apply -f k8s/db-service.yaml
kubectl apply -f k8s/app-deployment.yaml
kubectl apply -f k8s/app-service.yaml

echo "Recursos desplegados en el namespace fullstack-app"
kubectl get all -n fullstack-app
