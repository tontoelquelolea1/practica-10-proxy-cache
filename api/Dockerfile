# 1. Usamos una imagen base de Python ligera (slim)
FROM python:3.9-slim

# 2. Definimos la carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiamos el archivo de librerías para instalarlas
COPY requirements.txt .

# 4. Instalamos Flask y Redis sin guardar archivos basura (--no-cache-dir)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos el resto del código (app.py) a la carpeta /app
COPY . .

# 6. Comando final para arrancar nuestra API
CMD ["python", "app.py"]