from fastapi import FastAPI
from .routers import rerank
from pygaggle.rerank.transformer import MonoBERT

app = FastAPI()


app.state.reranker = MonoBERT()

# API endpoints
app.include_router(rerank.router, tags=["rerank"], prefix="/api")

@app.get("/api/status", status_code=200)
def status():
    return

@app.get("/api/.*", status_code=404, include_in_schema=False)
def invalid_api():
    return None