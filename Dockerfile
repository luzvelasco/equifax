# 1. Usar una imagen base oficial de Python
FROM python:3.10-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar las dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar el código de la aplicación
COPY app.py .

# 5. Exponer el puerto que usa la app
EXPOSE 8080

# 6. Comando para ejecutar la app (usando variables de entorno)
ENV TARGET="Prototipo AWS"
CMD ["python", "app.py"]