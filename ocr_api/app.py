from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from models.donut_infer import run_ocr
from PIL import Image
import io

app = FastAPI()

@app.post("/ocr")
async def ocr_endpoint(file: UploadFile = File(...)):
    print(f"Received file: {file.filename}, content-type: {file.content_type}")
    content = await file.read()
    print(f"File size: {len(content)} bytes")
    
    try:
        image = Image.open(io.BytesIO(content))
    except Exception as e:
        return JSONResponse(content={"error": f"Failed to open image: {str(e)}"})
    
    result = run_ocr(image)
    return JSONResponse(content=result)


@app.get("/")
async def hello_wolrd():
    hello = "Hello Wolrd"
    return JSONResponse(content=hello)