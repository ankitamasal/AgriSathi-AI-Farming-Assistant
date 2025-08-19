# src/backend/ingestion.py
# Simple ingestion + embedding builder for demo
import os
import json
from sentence_transformers import SentenceTransformer
import faiss

MODEL_NAME = "all-MiniLM-L6-v2"
RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data", "raw")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data")
INDEX_PATH = os.path.join(OUT_DIR, "faiss.index")
META_PATH = os.path.join(OUT_DIR, "meta.json")

def load_documents(folder=RAW_DIR):
    docs = []
    if not os.path.exists(folder):
        print("No raw data folder found:", folder)
        return docs
    for fname in os.listdir(folder):
        if fname.endswith(".txt") or fname.endswith(".json") or fname.endswith(".md"):
            with open(os.path.join(folder, fname), "r", encoding="utf-8") as f:
                docs.append({"source": fname, "text": f.read()})
    return docs

def build_embeddings(docs):
    if not docs:
        print("No documents to embed.")
        return
    model = SentenceTransformer(MODEL_NAME)
    texts = [d["text"] for d in docs]
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    faiss.write_index(index, INDEX_PATH)
    meta = [{"source": d["source"], "text": d["text"]} for d in docs]
    with open(META_PATH, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    print("Saved index and metadata to", OUT_DIR)

if __name__ == "__main__":
    docs = load_documents()
    build_embeddings(docs)
