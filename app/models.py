from pydantic import BaseModel
from typing import List

class QARequest(BaseModel):
    documents: str  # URL or path
    index_name: str
    questions: List[str]

class QAResponse(BaseModel):
    answers: List[str]
