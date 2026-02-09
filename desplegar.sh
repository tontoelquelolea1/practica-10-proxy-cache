#!/bin/bash
echo "🚀 Iniciando despliegue de la Práctica 10..."

# 1. Levantar contenedores
docker-compose up -d --build

# 2. Esperar un momento a que los servicios arranquen
echo "⏳ Esperando a que los servicios estén listos..."
sleep 5

# 3. Comprobación automática
echo "🔍 Verificando estado del servicio..."
STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost)

if [ $STATUS -eq 200 ]; then
    echo "✅ ¡ÉXITO! El proxy responde correctamente (HTTP 200)."
    echo "Prueba a ejecutar: curl -I http://localhost"
else
    echo "❌ ERROR: El servicio no responde (Código: $STATUS)."
fi