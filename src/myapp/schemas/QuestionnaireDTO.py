from pydantic import BaseModel
from typing import List
from src.myapp.AvailableFacts import InitialFacts

class QuestionDTO(BaseModel):
    question: str
    new_fact_if_true: InitialFacts

class QuestionnaireDTO(BaseModel):
    questions : List[QuestionDTO]