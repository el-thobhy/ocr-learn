# Base image Python
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install requirements
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy semua kode ke container
COPY . .

# Pindah ke folder project
WORKDIR /app/ocr_api

# Jalankan server, ambil port dari env Zeabur
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT}"]
