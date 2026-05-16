import pdfplumber
import pytesseract

from PIL import Image

from ai.entity_extractor import extract_entities

from ai.intelligence_retrieval_engine import (
    run_financial_investigation
)


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


def analyze_document(uploaded_file):

    text = extract_text(uploaded_file)

    entities = extract_entities(text)

    investigation = run_financial_investigation(
        text,
        entities
    )

    return {
        "entities": entities,
        "investigation_summary": investigation["summary"],
        "compliance_flags": investigation["flags"]
    }