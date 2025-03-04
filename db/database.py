"""from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://user:password@localhost/dbname"

engine = create_engine(DATABASE_URL) #, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()"""

import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
DB_FILE = os.getenv("DB", "comida.sqlite3")

engine = None

# Configuración de conexiones entre SQLAlchemy y SQLite3 DB API.
engine = create_engine(f"sqlite:///{DB_PATH}{DB_FILE}")

if "engine" in globals():
    # Creación de sesión con el engine de base de datos.
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Creación base declarativa.
    Base = declarative_base()