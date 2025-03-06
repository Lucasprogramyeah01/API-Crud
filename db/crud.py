from fastapi import HTTPException
from sqlalchemy.orm import Session
from db import model
from routers import comida

def findAll(db: Session):
    return db.query(model.tablaComida).all()

def findByID(db: Session, id: int):
    return db.query(model.tablaComida).filter(model.tablaComida.id == id).first()

def save(db: Session, comida: comida.Comida):
    if db.query(model.tablaComida).filter(model.tablaComida.nombre == comida.nombre).first():
        raise HTTPException(status_code=409, detail=f"No se ha podido agregar la comida, ya existe una con nombre: {comida.nombre}.")
    else:
        comidaDB = model.tablaComida(
            nombre = comida.nombre,
            paisProcedencia = comida.paisProcedencia,
            numIngredientes = comida.numIngredientes,
            precio = comida.precio
        )

        db.add(comidaDB)
        db.commit()
        db.refresh(comidaDB)

    return comidaDB

def edit(db: Session, id: int, comida: comida.Comida):
    if db.query(model.tablaComida).filter(model.tablaComida.nombre == comida.nombre).first():
        raise HTTPException(status_code=409, detail=f"No se ha podido editar la comida, ya existe una con nombre: {comida.nombre}.")
    else:
        comidaDB = db.query(model.tablaComida).filter(model.tablaComida.id == id).first()
        if comidaDB:
            comidaDB.nombre = comida.nombre
            comidaDB.paisProcedencia = comida.paisProcedencia
            comidaDB.numIngredientes = comida.numIngredientes
            comidaDB.precio = comida.precio

            db.commit()
            db.refresh(comidaDB)

    return comidaDB

def delete(db: Session, id: int):
    comidaDB = db.query(model.tablaComida).filter(model.tablaComida.id == id).first()
    if comidaDB:
        db.delete(comidaDB)
        db.commit()
    return comidaDB
