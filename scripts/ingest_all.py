import json
from pathlib import Path

from backend.ingestion.load_docs import load_pdf
from backend.ingestion.preprocess import clean_text
from backend.ingestion.chunker import chunk_text


RAW_DIR = "data/raw_docs"
OUTPUT_FILE = "data/processed_docs/chunks.json"


def ingest_documents():
    all_chunks = []
    chunk_id = 0

    for file in Path(RAW_DIR).glob("*.pdf"):
        doc = load_pdf(str(file))
        cleaned_text = clean_text(doc["text"])
        chunks = chunk_text(cleaned_text)

        for idx, chunk in enumerate(chunks):
            all_chunks.append({
                "chunk_id": chunk_id,
                "text": chunk,
                "source": doc["source"],
                "chunk_index": idx
            })
            chunk_id += 1

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=2)

    print(f"Ingested {len(all_chunks)} chunks")


if __name__ == "__main__":
    ingest_documents()
