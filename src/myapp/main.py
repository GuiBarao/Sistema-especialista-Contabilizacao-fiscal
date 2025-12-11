from fastapi import FastAPI
from src.myapp.routes.ConsultRouter import ConsultRouter
app = FastAPI()


app.include_router(ConsultRouter().router)