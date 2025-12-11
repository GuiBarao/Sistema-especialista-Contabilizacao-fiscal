from fastapi import APIRouter
from src.myapp.services.ConsultService import ConsultService
from src.myapp.schemas.ConsultDTO import ResultQuestionnaireDTO, ResultClipsDTO
from src.myapp.schemas.QuestionnaireDTO import QuestionnaireDTO
class ConsultRouter:

    def __init__(self):
        self.__service = ConsultService()

        self.router = APIRouter(prefix="/consult")

        self.router.post("/")(self.consult)
        self.router.get("/")(self.questionnaire)

    def consult(self, initial_data: ResultQuestionnaireDTO) -> ResultClipsDTO:
        return self.__service.avaliate(initial_data)
    
    def questionnaire(self) -> dict:
        return self.__service.get_questions()


