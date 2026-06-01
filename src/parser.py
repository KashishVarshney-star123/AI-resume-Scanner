# Resume text extraction parser supporting PDF and DOCX.
import fitz  # PyMuPDF
import docx2txt

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using PyMuPDF."""
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
    except Exception as e:
        print(f"Error reading PDF {pdf_path}: {e}")
    return text

def extract_text_from_docx(docx_path):
    """Extract text from a DOCX file using docx2txt."""
    try:
        return docx2txt.process(docx_path)
    except Exception as e:
        print(f"Error reading DOCX {docx_path}: {e}")
        return ""
