from flask import Flask, jsonify
import redis
import time
import os

app = Flask(__name__)

# Conexión a Redis usando el nombre del host de Docker
# Esto permite la comunicación interna en la red privada
cache = redis.Redis(host='redis-server', port=6379) [cite: 69]

@app.route('/')
def index():
    try:
        # INTENTO 1: Consultar Caché Nivel 2 (Redis)
        # Es muy rápido (milisegundos)
        data = cache.get('datos_procesados')
        
        if data:
            # CACHE HIT (Redis): Devolvemos el dato guardado
            return jsonify({
                "source": "Redis Cache (Nivel 2) - Rápido",
                "data": data.decode('utf-8')
            })
        
        # INTENTO 2: CACHE MISS (Redis) -> Procesar
        # Simulamos un proceso pesado de 3 segundos (Requisito de la práctica)
        time.sleep(3) [cite: 68]
        result = "Estos datos costaron 3 segundos en generarse."
        
        # Guardamos el resultado en Redis para el futuro
        cache.set('datos_procesados', result) [cite: 69]
        
        return jsonify({
            "source": "API Backend (Python) - Lento",
            "data": result
        })
            
    except redis.ConnectionError:
        return jsonify({"error": "No se pudo conectar a Redis"}), 500

if __name__ == '__main__':
    # Escuchamos en 0.0.0.0 para aceptar conexiones externas (del proxy)
    app.run(host='0.0.0.0', port=8080)