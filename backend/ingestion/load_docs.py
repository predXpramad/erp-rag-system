import pdfplumber
from pathlib import Path


def load_pdf(file_path: str) -> dict:
    """
    Loads PDF and returns text with metadata
    """
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            page_text = page.extract_text()
            if page_text:
                text += f"\n[Page {page_num + 1}]\n{page_text}"

    return {
        "text": text,
        "source": Path(file_path).name
    }
