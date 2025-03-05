from sqlalchemy.orm import Session
from db import model
from routers import comida

def findAll(db: Session):
    return db.query(model.tablaComida).all()

def findByID(db: Session, id: int):
    return db.query(model.tablaComida).filter(model.tablaComida.id == id).first()

def save(db: Session, comida: comida.Comida):
    comidaDB = model.tablaComida(**comida.dict())
    db.add(comidaDB)
    db.commit()
    db.refresh(comidaDB)
    return comidaDB

