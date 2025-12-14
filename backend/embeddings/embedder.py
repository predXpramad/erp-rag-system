import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from pathlib import Path


MODEL_NAME = "all-MiniLM-L6-v2"
DATA_PATH = "data/processed_docs/chunks.json"
INDEX_PATH = "backend/vector_store/faiss_index/index.faiss"
META_PATH = "backend/vector_store/faiss_index/metadata.json"


def build_faiss_index():
    # Load chunks
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    texts = [chunk["text"] for chunk in chunks]

    # Load embedding model
    model = SentenceTransformer(MODEL_NAME)
    embeddings = model.encode(texts, show_progress_bar=True)

    embeddings = np.array(embeddings).astype("float32")

    # Create FAISS index
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    # Save index
    faiss.write_index(index, INDEX_PATH)

    # Save metadata
    with open(META_PATH, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2)

    print(f"FAISS index built with {index.ntotal} vectors")


if __name__ == "__main__":
    build_faiss_index()
