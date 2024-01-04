# Utiliza la imagen oficial de Python 3.9
FROM python:3.12.0

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el código de la aplicación a la imagen
COPY . /app

# Instala las dependencias de la aplicación
RUN pip install -r requirements.txt

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 8721

# Comando para ejecutar la aplicación FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8721"]
