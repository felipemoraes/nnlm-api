from typing import List, Dict
from fastapi import APIRouter, Request
from app.models import RerankResponse, RerankRequest, Doc
from pygaggle.rerank.base import Query, Text

router = APIRouter()

@router.post('/rerank', response_model=RerankResponse)
async def rerank(rerank_request: RerankRequest, request: Request):
    query = Query(rerank_request.query)
    texts = [ Text(doc.content, {'docid': doc.docid}, 0) for doc in rerank_request.docs]
    reranked = request.app.state.reranker.rerank(query, texts)
    reranked.sort(key=lambda x: x.score, reverse=True)
    results = [Doc(docid=doc.metadata["docid"], score=doc.score) for doc in reranked]
    response = RerankResponse(query=rerank_request.query, docs=results)
    return response