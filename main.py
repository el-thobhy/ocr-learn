from fastapi import FastAPI
from app.api.v1 import routes_ocr
from app.core.config import settings

app = FastAPI(title="OCR API", version="1.0")

#register route
app.include_router(routes_ocr.router, prefix="/api/v1/ocr")