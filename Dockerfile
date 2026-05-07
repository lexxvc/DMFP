# Dockerfile for RAG Asistente Ecommerce (Gradio + ChromaDB + Gemini)
# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy application code
COPY . .

# Expose Gradio default port
EXPOSE 7860

# Set Gradio to listen on all interfaces for Cloud Run
ENV GRADIO_SERVER_NAME=0.0.0.0

# Command to run the Gradio app (update if your main file changes)
CMD ["python", "RAG_Asistente_Ecommerce(1).ipynb"]
