# Usar una imagen base de Python
FROM python:3.12-slim-buster

# Establecer un directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Ejecutar el script de Python al iniciar el contenedor
CMD ["python", "./apiDeamon.py"]