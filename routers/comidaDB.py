from typing import Annotated
from fastapi import APIRouter, Depends
from db.database import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter(prefix="/comidaDB",
                   tags=["comidaDB"])

def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

dbDependency = Annotated[Session, Depends(getDB)]

