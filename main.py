from fastapi import FastAPI
from routers import comida, comidaDB

app = FastAPI()

app.include_router(comida.router)
app.include_router(comidaDB.router)
