from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db import crud
from db.database import getDB
from routers import comida

router = APIRouter(prefix="/comidaDB",
                   tags=["comidaDB"])

# findAll
@router.get("/", response_model=List[comida.Comida])
def findAll(db: Session = Depends(getDB)):
    return crud.findAll(db)

# findByID
@router.get("/{id}", response_model=comida.Comida)
def findByID(id: int, db: Session = Depends(getDB)):
    comidaEncontrada = crud.findByID(db, id)
    if comidaEncontrada is None:
        raise HTTPException(status_code=404, detail=f"No se encontrado ninguna comida con ID: {id}.")
    return comidaEncontrada

# save
@router.post("/", response_model=comida.Comida)
def save(comida: comida.Comida, db: Session = Depends(getDB)):
    return crud.save(db, comida)

# edit
@router.put("/{id}", response_model=comida.Comida)
def edit(id: int, comidaActualizada: comida.Comida, db: Session = Depends((getDB))):
    comidaEditada = crud.edit(db, id, comidaActualizada)
    if comidaEditada is None:
        raise HTTPException(status_code=404, detail=f"No se encontrado ninguna comida con ID: {id}.")
    return comidaEditada

# delete
@router.delete("/{id}", response_model=comida.Comida)
def delete(id: int, db: Session = Depends(getDB)):
    comidaBorrada = crud.delete(db, id)
    if comidaBorrada is None:
        raise HTTPException(status_code=404, detail=f"No se encontrado ninguna comida con ID: {id}.")
    return comidaBorrada
