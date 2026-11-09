import openbharatocr
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def extract_aadhaar(image_path):

    image = Image.open(image_path)

    # Check raw OCR output
    # text = pytesseract.image_to_string(image)

    # print("\n--- RAW OCR TEXT ---")
    # print(text)
    # print("-------------------\n")

    result = openbharatocr.front_aadhaar(image_path)

    print("OpenBharatOCR result:", result)

    return result