from fastapi import FastAPI
from pydantic import BaseModel
from backend.vector_store.search import VectorSearch
from backend.rag.prompt_template import build_prompt
from backend.llm.llm_client import generate_answer
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI(
    title="ERP RAG QA System",
    description="Lightweight RAG-based QA for ERP Manuals",
    version="1.0"
)
app.mount(
    "/static",
    StaticFiles(directory="backend/frontend"),
    name="static"
)

vector_search = VectorSearch()

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str
    sources: list


@app.get("/health")
def health_check():
    return {"status": "OK"}


@app.post("/ask", response_model=AnswerResponse)
def ask_question(req: QuestionRequest):
    results = vector_search.search(req.question, top_k=3)

    context_chunks = [r["text"] for r in results]
    sources = list({r["source"] for r in results})

    prompt = build_prompt(req.question, context_chunks)
    answer = generate_answer(prompt)

    return AnswerResponse(
        answer=answer,
        sources=sources
    )

@app.get("/", response_class=HTMLResponse)
def serve_ui():
    html_path = Path("backend/frontend/index.html")
    return html_path.read_text(encoding="utf-8")
