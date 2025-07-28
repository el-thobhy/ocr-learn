# Base image Python
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install requirements
COPY requirements.txt .
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libgl1 \
    && pip install --upgrade pip && pip install -r requirements.txt


# Copy semua kode ke container
COPY . .

# Jalankan server saat container start
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT}"]
