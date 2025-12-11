from src.myapp.ClipsInterface import ClipsInterface
from src.myapp.schemas.ConsultDTO import QuestionnaireDTO, ResultDTO
from src.myapp.AvailableFacts import ResultFacts
from typing import List

class ConsultService:
    
    def __init__(self):
        self.__clips = ClipsInterface()


    def avaliate(self, initial_data: QuestionnaireDTO) -> ResultDTO:

        for fact in initial_data.questionnaire_result:
            self.__clips.insert_new_fact(f"({fact.value})")

        self.__clips.run_inference()

        raw_result_facts: List[str] = list(filter( lambda fact: 
                                                    fact not in initial_data.questionnaire_result, 
                                                    self.__clips.actual_facts()))
        
        result_facts : List[ResultFacts] = list(map(ResultFacts, raw_result_facts))

        return ResultDTO(tax_classification=result_facts)
    