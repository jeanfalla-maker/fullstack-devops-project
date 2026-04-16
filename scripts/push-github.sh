#!/bin/bash
set -e

if [ ! -f .env ]; then
  echo "No existe el archivo .env"
  echo "Copia .env.example a .env y edítalo."
  exit 1
fi

source .env

if [ -z "$GITHUB_REPO_URL" ]; then
  echo "La variable GITHUB_REPO_URL no está definida en .env"
  exit 1
fi

if [ ! -d .git ]; then
  echo "Inicializando repositorio Git..."
  git init
fi

echo "Agregando archivos..."
git add .

echo "Creando commit..."
git commit -m "Proyecto full stack con Docker, Compose, Kubernetes y Bash" || echo "Nada nuevo para commit"

echo "Configurando rama principal..."
git branch -M main

echo "Configurando remote origin..."
if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$GITHUB_REPO_URL"
else
  git remote add origin "$GITHUB_REPO_URL"
fi

echo "Remote actual:"
git remote -v

echo "Subiendo proyecto a GitHub..."
git push -u origin main || {
  echo ""
  echo "Error al subir a GitHub."
  echo "Verifica:"
  echo "1. Que el repositorio exista en GitHub"
  echo "2. Que GITHUB_REPO_URL sea correcta"
  echo "3. Que uses Token o SSH, no contraseña"
  exit 1
}

echo "Proyecto publicado correctamente en GitHub."
