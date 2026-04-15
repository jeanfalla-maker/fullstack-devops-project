#!/bin/bash
set -e

echo "Desplegando stack con Docker Compose..."
docker compose up -d --build

echo "Servicios activos:"
docker compose ps

echo "Aplicación disponible en: http://localhost:5000"
