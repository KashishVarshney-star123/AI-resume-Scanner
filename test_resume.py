import fitz
import docx2txt
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
POPPLER_PATH = r'C:\poppler\Library\bin'

pdf_path = "uploads/Kashish_resume.pdf"

print("PDF khol raha hai...")
images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
print(f"Total pages: {len(images)}")

text = ""
for i, img in enumerate(images):
    page_text = pytesseract.image_to_string(img)
    print(f"Page {i+1} text length: {len(page_text)}")
    print(f"Page {i+1} sample: {page_text[:200]}")
    text += page_text

print("=== TOTAL TEXT LENGTH ===")
print(len(text))