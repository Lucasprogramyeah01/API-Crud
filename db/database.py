from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "sqlite:///./comida.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependencia para obtener la sesión de la Base de Datos.
def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ejecuta el "import.sql" al iniciar el servidor.
def ejecutarImportSQL():
    sql_file = "./db/import.sql" 
    if os.path.exists(sql_file):
        with engine.connect() as connection:
            with open(sql_file, "r", encoding="utf-8") as file:
                sql_script = file.read()
                connection.execute(text(sql_script))
            connection.commit()
        print("El archivo import.sql se ha ejecutado correctamente.")
