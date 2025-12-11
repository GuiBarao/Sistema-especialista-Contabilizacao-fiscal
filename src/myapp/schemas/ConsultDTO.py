from pydantic import BaseModel
from src.myapp.AvailableFacts import ResultFacts, InitialFacts
from typing import List

class QuestionnaireDTO(BaseModel):
    questionnaire_result: List[InitialFacts]


class ResultDTO(BaseModel):
    tax_classification: List[ResultFacts]