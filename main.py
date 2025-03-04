from fastapi import FastAPI
from routers import comida
from db import model
from db.database import engine

app = FastAPI()
model.Base.metadata.create_all(bind=engine)

app.include_router(comida.router)
