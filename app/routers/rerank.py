from typing import List
from fastapi import APIRouter
from app.services import reranker
from app.models import SearchQueryResponse, SearchQueryRequest
router = APIRouter()

@router.post('/rerank', response_model=SearchQueryResponse)
async def rerank(request: SearchQueryResponse):
    results = reranker(request.query, request.docs)
    response = SearchQueryResponse(query=request.query, docs=results)
    return response