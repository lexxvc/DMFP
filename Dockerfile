# Usa una imagen ligera de Python
FROM python:3.10-slim

# Directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Expone el puerto que usa Cloud Run
EXPOSE 8080

# Comando para iniciar la app
CMD ["python", "RAG.py"]
