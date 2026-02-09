# Práctica 10 - Proxy Inverso y Caché (SAD)

## 1. Descripción
Este proyecto implementa una infraestructura de microservicios diseñada para optimizar el rendimiento y la seguridad. 
Utiliza un Proxy Inverso (Nginx) con caché de Nivel 1, una API en Flask y una base de datos Redis como caché de Nivel 2.

## 2. Diagrama de Arquitectura

```text
       SEGURIDAD PERIMETRAL (Toda la red está protegida)
      ┌─────────────────────────────────────────────────────────┐
      │  RED PRIVADA DOCKER (bridge) - IP: 172.x.x.x            │
      │                                                         │
      │  ┌───────────────┐        ┌───────────────┐             │
      │  │               │        │               │             │
Petición │    NGINX      │ Proxy  │  API PYTHON   │             │
Usuario  │ (Puerto 80)  ─┼───────►│ (Puerto 8080) │             │
 ───────►│               │ Pass   │    (Flask)    │             │
         │  [Caché L1]   │        │               │             │
         └───────────────┘        └───────┬───────┘             │
                                          │                     │
                                          │ Consulta            │
                                          │ Caché               │
                                          ▼                     │
                                  ┌───────────────┐             │
                                  │               │             │
                                  │     REDIS     │             │
                                  │ (Puerto 6379) │             │
                                  │  [Caché L2]   │             │
                                  │               │             │
                                  └───────────────┘             │
      └─────────────────────────────────────────────────────────┘
```
## 3. Scripts de Automatización y Recuperación
Para facilitar la gestión del entorno y asegurar la disponibilidad ante fallos, se han incluido scripts de Bash:

* **`./desplegar.sh`**: Automatiza el ciclo de vida del despliegue.
  - Levanta los contenedores con `docker-compose up -d --build`.
  - Espera a que los servicios arranquen.
  - Realiza un test de conexión (`curl`) para confirmar que el proxy responde correctamente (HTTP 200).

* **`./recuperar.sh`**: Implementa una política de **Disaster Recovery**.
  - Si se elimina accidentalmente algún archivo de configuración crítico (ej: `docker-compose.yml`), este script restaura la última versión estable directamente desde el repositorio Git local.

> **Nota:** Recuerda dar permisos de ejecución antes de usarlos con el comando: `chmod +x *.sh`

## 4. Instrucciones de Despliegue
Para levantar el entorno en clase, sigue estos pasos:

1. Clonar el repositorio:
   `git clone https://github.com/tontoelquelolea1/practica-10-proxy-cache.git`
2. Entrar en la carpeta:
   `cd practica-10-proxy-cache`
3. Levantar los contenedores:
   `docker-compose up -d --build`

## 4. Pruebas de Verificación
Para comprobar el funcionamiento de las capas de caché:
- **MISS (Lento):** La primera petición a `http://localhost` tardará ~3s (el backend procesa).
- **HIT (Rápido):** Las siguientes peticiones serán instantáneas gracias a Nginx y Redis.
- **Seguridad:** Intentar entrar a `http://localhost:8080` debe fallar, cumpliendo la seguridad perimetral definida en la práctica.