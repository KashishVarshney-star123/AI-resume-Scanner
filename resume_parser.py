import fitz
import docx2txt
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
POPPLER_PATH = r'C:\poppler\Library\bin'

def extract_text(file_path):
    text = ""
    
    if file_path.endswith(".pdf"):
        try:
            doc = fitz.open(file_path)
            for page in doc:
                text += page.get_text()
        except:
            pass
        
        if len(text.strip()) < 50:
            try:
                images = convert_from_path(
                    file_path,
                    poppler_path=POPPLER_PATH
                )
                for img in images:
                    text += pytesseract.image_to_string(img)
            except Exception as e:
                print(f"OCR Error: {e}")
    
    elif file_path.endswith(".docx"):
        text = docx2txt.process(file_path)
    
    return text.strip()