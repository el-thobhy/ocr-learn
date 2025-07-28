# Base image Python
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file dan install semua dependensi
COPY requirements.txt .
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libgl1 \
    && pip install --upgrade pip && pip install -r requirements.txt


# Salin semua kode ke container
COPY . .

# Jalankan server saat container start
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "${PORT}"]
