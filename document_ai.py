import pdfplumber
import pytesseract
from PIL import Image
import tempfile


def extract_text(uploaded_file):

    text = ""

    if uploaded_file.type == "application/pdf":
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

    else:
        image = Image.open(uploaded_file)
        text = pytesseract.image_to_string(image)

    return text


from rag_engine import run_rag


def analyze_document(uploaded_file):

    text = extract_text(uploaded_file)

    llm_response = run_rag(text)

    return {
        "sender_name": "Extracted via AI",
        "country": "Detected",
        "amount": "Detected",
        "risk_flag": llm_response
    }