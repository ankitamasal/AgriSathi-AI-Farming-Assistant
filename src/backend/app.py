# src/backend/app.py
from fastapi import FastAPI
from pydantic import BaseModel
from retriever import Retriever
import os

app = FastAPI()
retriever = Retriever()

class Query(BaseModel):
    text: str
    lang: str = "en"

@app.post("/ask")
def ask(q: Query):
    docs = retriever.retrieve(q.text, top_k=4)
    context = "\n\n".join([f"[{d['source']}]\n{d['text'][:1000]}" for d in docs])
    prompt = f"""You are AgriSathi, an expert agricultural assistant. Use only the facts below.
User question: {q.text}

Facts:
{context}

Answer in short bullets (max 6), then list sources. If unknown, say "I don't know — check source".
"""
    # NOTE: Integrate with your chosen LLM here (OpenAI, local model, etc.)
    response_text = "DEMO: This endpoint would call the LLM with the prompt and return answer + sources."
    return {"answer": response_text, "sources": [d["source"] for d in docs]}
