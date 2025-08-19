# src/backend/retriever.py
import os, json
from sentence_transformers import SentenceTransformer
import faiss

MODEL_NAME = "all-MiniLM-L6-v2"
BASE = os.path.join(os.path.dirname(__file__), "..", "..")
INDEX_PATH = os.path.join(BASE, "data", "faiss.index")
META_PATH = os.path.join(BASE, "data", "meta.json")

class Retriever:
    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)
        if os.path.exists(INDEX_PATH):
            self.index = faiss.read_index(INDEX_PATH)
        else:
            self.index = None
        if os.path.exists(META_PATH):
            with open(META_PATH, "r", encoding="utf-8") as f:
                self.meta = json.load(f)
        else:
            self.meta = []

    def retrieve(self, query, top_k=5):
        if not self.index:
            return []
        q_emb = self.model.encode([query], convert_to_numpy=True)
        D, I = self.index.search(q_emb, top_k)
        results = []
        for idx in I[0]:
            if idx < len(self.meta):
                results.append(self.meta[idx])
        return results
