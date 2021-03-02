from typing import List
from pydantic import BaseModel



class Doc(BaseModel):
    docid: str
    score: float

class RerankResponse(BaseModel):
    query: str
    docs: List[Doc]

class DocContent(BaseModel):
    docid: str
    content: str

class RerankRequest(BaseModel):
    query: str
    docs: List[DocContent]