# ===== app/services/ocr_service.py =====
import pytesseract
from PIL import Image
import io
import cv2
import numpy as np

# (Optional) Set path to tesseract executable if on Windows
# pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def preprocess_image(image_bytes):
    img_array = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return Image.fromarray(binary)

async def run_ocr(file):
    image_bytes = await file.read()
    image = preprocess_image(image_bytes)
    text = pytesseract.image_to_string(image, lang='eng')  # gunakan 'ind' untuk bahasa Indonesia
    return {"text": text}