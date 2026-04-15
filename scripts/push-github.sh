#!/bin/bash
set -e

if [ ! -f .env ]; then
  echo "No existe el archivo .env. Copia .env.example a .env y edítalo."
  exit 1
fi

source .env

if [ ! -d .git ]; then
  git init
fi

git add .
git commit -m "Proyecto full stack con Docker, Compose, Kubernetes y Bash" || echo "Nada nuevo para commit"
git branch -M main
git remote remove origin 2>/dev/null || true
git remote add origin "$GITHUB_REPO_URL"
git push -u origin main
