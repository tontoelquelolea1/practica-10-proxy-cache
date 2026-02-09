#!/bin/bash
# Script de despliegue y verificacion automatica

# Levanta los contenedores en segundo plano recreando imagenes si hay cambios
sudo docker compose up -d --build --remove-orphans

# Tiempo de espera para asegurar el arranque de los servicios
sleep 5

# Verificacion del estado del Proxy mediante codigo de respuesta HTTP
STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost)

if [ $STATUS -eq 200 ]; then
    echo "Despliegue correcto: El proxy responde (HTTP 200)"
else
    echo "Error en el despliegue: Codigo de respuesta $STATUS"
fi