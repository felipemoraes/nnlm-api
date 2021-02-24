from typing import List
from pygaggle.rerank.base import Query, Text
from models import Doc, DocScored

def reranker(query: str, docs: List[Doc]):
    query = Query(query)
    texts = [ Text(doc.content, {'docid': doc.docid}, 0) for doc in docs]
    reranked = app.state.reranker.rerank(query, texts)
    reranked.sort(key=lambda x: x.score, reverse=True)
    docs_scored = [DocScored(docid=doc.metadata["docid"], score=doc.score)]
    return docs_scored