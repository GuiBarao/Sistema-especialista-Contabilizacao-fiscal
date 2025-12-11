from fastapi import APIRouter
from src.myapp.services.ConsultService import ConsultService
from src.myapp.schemas.ConsultDTO import QuestionnaireDTO, ResultDTO

class ConsultRouter:

    def __init__(self):
        self.__service = ConsultService()

        self.router = APIRouter(prefix="/consult")

        self.router.post("/")(self.consult)

    def consult(self, initial_data: QuestionnaireDTO) -> ResultDTO:
        return self.__service.avaliate(initial_data)


