from fastapi import FastAPI
from db.database import engine
from db import model, database
from routers import comida, comidaDB
import os

# Crea las tables y ejecuta el "import.sql" sólo si no existe el archivo "comida.db".
def initialize_db():
    if not os.path.exists('comida.db'):
        print("Inicializando la base de datos...")
        model.Base.metadata.create_all(bind=engine)
        database.ejecutarImportSQL()
    else:
        print("La base de datos ya está creada, no es necesario inicializarla.")

initialize_db()

app = FastAPI()

app.include_router(comida.router)
app.include_router(comidaDB.router)
