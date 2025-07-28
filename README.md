# ===== README.md =====
# OCR API

FastAPI backend for OCR processing.

## Usage
```
docker build -t ocr-api .
docker run -p 8000:8000 ocr-api
```

## Endpoint
POST /api/v1/ocr/predict
- Form file: `file`
- Response: `{ "text": "..." }`

## Model
Menggunakan Tesseract OCR dengan preprocessing OpenCV (threshold binarization)
