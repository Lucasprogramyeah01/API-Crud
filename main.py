from fastapi import FastAPI
from routers import comida, comidaDB
from db.database import SessionLocal, engine
from db.model import Base

app = FastAPI()

app.include_router(comida.router)
app.include_router(comidaDB.router)

