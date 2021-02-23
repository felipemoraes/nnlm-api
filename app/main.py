from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/api")
async def read_root():
    return {"API": "API is up and urnning"}


class Doc(BaseModel):
    doc_id: str
    score: float

class SearchQueryRequest(BaseModel):
    query: str
    docs: List[Doc]

class SearchQueryResponse(BaseModel):
    query: str
    docs: List[Doc]


@app.post('/api/rerank', response_model=SearchQueryResponse)
async def rerank(request: SearchQueryResponse):
    response = SearchQueryResponse(query=request.query, docs=request.docs)
    return response