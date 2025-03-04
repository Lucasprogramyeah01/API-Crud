from fastapi import FastAPI
from routers import comida

app = FastAPI()

app.include_router(comida.router)