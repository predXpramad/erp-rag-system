import re


def clean_text(text: str) -> str:
    """
    Basic text cleaning
    """
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\n+", "\n", text)
    return text.strip()
