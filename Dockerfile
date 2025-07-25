# Base image Python
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file dan install semua dependensi
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r ocr_api/requirements.txt

# Salin semua kode ke container
COPY . .

# Masuk ke folder tempat app.py berada
WORKDIR /app/ocr_api

# Expose port FastAPI
EXPOSE 8000

# Jalankan server saat container start
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
