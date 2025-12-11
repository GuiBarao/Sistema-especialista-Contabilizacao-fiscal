from src.myapp.ClipsInterface import ClipsInterface
from src.myapp.schemas.ConsultDTO import ResultQuestionnaireDTO, ResultClipsDTO
from src.myapp.schemas.QuestionnaireDTO import QuestionnaireDTO
from src.myapp.AvailableFacts import ResultFacts
from typing import List
import json

class ConsultService:
    
    def __init__(self):
        self.__clips = ClipsInterface()


    def avaliate(self, initial_data: ResultQuestionnaireDTO) -> ResultClipsDTO:

        for fact in initial_data.questionnaire_result:
            self.__clips.insert_new_fact(f"({fact.value})")

        self.__clips.run_inference()

        raw_result_facts: List[str] = list(filter( lambda fact: 
                                                    fact not in initial_data.questionnaire_result, 
                                                    self.__clips.actual_facts()))
        
        result_facts : List[ResultFacts] = list(map(ResultFacts, raw_result_facts))

        return ResultClipsDTO(tax_classification=result_facts)
    

    def get_questions(self) -> dict:

        with open("src/myapp/resources/questionnaire.json", "r", encoding="UTF-8") as arq:
            json_arq = json.load(arq)

        return json_arq


