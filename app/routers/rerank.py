from typing import List
from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

class Doc(BaseModel):
    doc_id: str
    score: float

class SearchQueryRequest(BaseModel):
    query: str
    docs: List[Doc]

class SearchQueryResponse(BaseModel):
    query: str
    docs: List[Doc]


@router.post('/rerank', response_model=SearchQueryResponse)
async def rerank(request: SearchQueryResponse):
    response = SearchQueryResponse(query=request.query, docs=request.docs)
    return response