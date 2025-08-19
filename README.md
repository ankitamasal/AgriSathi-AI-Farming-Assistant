# AgriSathi-AI-Farming-Assistant
AI-powered farming advisor using RAG, multilingual support, and open agri-datasets to help farmers make smarter crop, weather, and finance decisions.
# AgriSathi — AI Advisor for Farmers

## Overview
AgriSathi is an AI agent that answers farming queries by combining public data (weather, soil, crop calendar, pests, market prices) with a retrieval-augmented LLM. Answers are short, actionable, cited, and available via web + WhatsApp/SMS.

## Features
- Multilingual Q&A (English, Hindi, Marathi)
- Retrieval-backed answers with source citations
- Action checklist, confidence and risk flag
- Low-bandwidth fallback via SMS/WhatsApp
- Admin dashboard to review queries & update datasets

## Quick start (dev)
1. Create virtual env: `python -m venv venv && source venv/bin/activate`
2. Install: `pip install -r src/backend/requirements.txt`
3. Prepare embeddings: run `python src/backend/ingestion.py --build-embeddings`
4. Start backend: `uvicorn src.backend.app:app --reload`
5. Start frontend: `cd src/frontend/react-app && npm install && npm start`

## Data
Place raw dataset files in `data/raw/`. Cite sources in `docs/sources.md`.

## How it works
- Ingestion normalizes datasets into text facts.
- `embedder.py` creates embeddings and FAISS index.
- `retriever.py` returns top-K documents for a query.
- `prompt.py` crafts the instruction for the LLM with retrieved facts.
- `app.py` exposes a REST endpoint `/ask` which returns answer + sources.

## Demo
See `demos/demo_script.md` for sample queries and flows to show during hackathon.

## License
MIT

## Team
Ankita (lead)
