import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"
INDEX_PATH = "backend/vector_store/faiss_index/index.faiss"
META_PATH = "backend/vector_store/faiss_index/metadata.json"


class VectorSearch:
    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)
        self.index = faiss.read_index(INDEX_PATH)

        with open(META_PATH, "r", encoding="utf-8") as f:
            self.metadata = json.load(f)

    def search(self, query: str, top_k=3):
        query_embedding = self.model.encode([query])
        query_embedding = np.array(query_embedding).astype("float32")

        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx in indices[0]:
            item = self.metadata[idx]
            results.append({
                "text": item["text"],
                "source": item["source"],
                "chunk_id": item["chunk_id"]
            })

        return results
