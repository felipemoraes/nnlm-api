from typing import List
from pydantic import BaseModel


class Doc(BaseModel):
    docid: str
    content: str

class DocScored(BaseModel):
    docid: str
    score: float

class SearchQueryRequest(BaseModel):
    query: str
    docs: List[Doc]

class SearchQueryResponse(BaseModel):
    query: str
    docs: List[DocScored]