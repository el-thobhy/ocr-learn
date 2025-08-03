# ===== README.md =====
# OCR API

FastAPI backend for OCR processing.

## Usage
```
docker build -t python-ocr .
docker run --name fastapi-container -e PORT=8000 -p 8000:8000 python-ocr
```

## Endpoint
POST /api/v1/ocr/predict
- Form file: `file`
- Response: `{ "text": "..." }`

## Model
Menggunakan Tesseract OCR dengan preprocessing OpenCV (threshold binarization)
