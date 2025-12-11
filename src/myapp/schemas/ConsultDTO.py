from pydantic import BaseModel
from src.myapp.AvailableFacts import ResultFacts, InitialFacts
from typing import List

class ResultQuestionnaireDTO(BaseModel):
    questionnaire_result: List[InitialFacts]


class ResultClipsDTO(BaseModel):
    tax_classification: List[ResultFacts]