from backend.vector_store.search import VectorSearch

searcher = VectorSearch()

query = "List Components Required to Build an ML Model."

results = searcher.search(query)

for r in results:
    print("SOURCE:", r["source"])
    print("TEXT:", r["text"][:200])
    print("-" * 40)
