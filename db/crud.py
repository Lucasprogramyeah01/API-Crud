from sqlalchemy.orm import Session
from db import model
from routers import comida

def findAll(db: Session):
    return db.query(model.tablaComida).all()

def findByID(db: Session, id: int):
    return db.query(model.tablaComida).filter(model.tablaComida.id == id).first()

def save(db: Session, comida: comida.Comida):
    comidaDB = model.tablaComida(**comida.model_dump())
    db.add(comidaDB)
    db.commit()
    db.refresh(comidaDB)
    return comidaDB

def edit(db: Session, id: int, comidaEditada: comida.Comida):
    comidaDB = db.query(model.tablaComida).filter(model.tablaComida.id == id).first()
    if comidaDB:
        for key, value in comidaEditada.model_dump().items():
            setattr(comidaDB, key, value)
        db.commit()
        db.refresh(comidaDB)
    return comidaDB

def delete(db: Session, id: int):
    comidaDB = db.query(model.tablaComida).filter(model.tablaComida.id == id).first()
    if comidaDB:
        db.delete(comidaDB)
        db.commit()
    return comidaDB
