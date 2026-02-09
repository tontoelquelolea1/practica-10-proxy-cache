from flask import Flask, jsonify
import redis
import time
import os

app = Flask(__name__)

# Conecta al contenedor 'redis' usando el puerto estándar 6379
cache = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=6379)

@app.route('/')
def index():
    # PASO 1: Buscar en Caché L2 (Redis)
    cached_res = cache.get('data')
    if cached_res:
        return jsonify({"data": cached_res.decode('utf-8'), "source": "Redis Cache (Nivel 2)"})

    # PASO 2: Si no está en caché, "trabajar" (simula proceso pesado)
    time.sleep(3)
    data = "Resultado de operacion pesada"
    
    # PASO 3: Guardar en Redis por 300 segundos para la próxima vez
    cache.setex('data', 300, data)
    
    return jsonify({"data": data, "source": "API Backend (Calculado)"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) # Escucha en todas las IPs del contenedor