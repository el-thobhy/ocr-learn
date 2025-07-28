from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from app.services.ocr_services import run_ocr

router = APIRouter()

@router.post("/predict")
async def predict_ocr(file: UploadFile = File(...)):
    return await run_ocr(file)


@router.get("/")
async def hello_wolrd():
    hello = "Hello Wolrd"
    return JSONResponse(content=hello)