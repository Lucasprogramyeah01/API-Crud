from fastapi import APIRouter, FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal, engine
from db.model import tablaComida, Base
from db.crud import findAll, findByID, save

router = APIRouter(prefix="/comidaDB",
                   tags=["comidaDB"])

# Creación de tablas en la Base de Datos.
Base.metadata.create_all(bind=engine)

# Dependencia para obtener la sesión de la Base de Datos.
def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# findAll_DB
@router.get("/")
async def findAll_DB(db: Session = Depends(getDB)):
    return findAll(db)

# findByID_DB
@router.get("/{id}")
async def findByID_DB(id: int, db: Session = Depends(getDB)):
    comida = findByID(db, id)
    if comida is None:
        raise HTTPException(status_code=404, detail=f"No se ha podido encontrar una comida con ID: {id}.")
    return comida

# save_DB
@router.post("/")
async def save_DB(id: int, nombre: str, paisProcedencia: str, numIngredientes: int, 
    precio: float, db: Session = Depends(getDB)):
    return save(db, id, nombre, paisProcedencia, numIngredientes, precio)

# edit_DB
@router.put("/")
async def edit_DB(id: int, nombre: str, paisProcedencia: str, numIngredientes: int,
    precio: float, db: Session = Depends(getDB)):

    comida = db.query(tablaComida).filter(tablaComida.id == id).first()
    if comida is None:
        raise HTTPException(status_code=404, detail=f"No se ha podido encontrar una comida con ID: {id}.")
    
    comida.id = id
    comida.nombre = nombre
    comida.paisProcedencia = paisProcedencia
    comida.numIngredientes = numIngredientes
    comida.precio = precio
    db.commit()
    db.refresh(comida)
    
    return comida

# delete_DB
@router.delete("/{id}")
async def delete_DB(id: int, db: Session = Depends(getDB)):
    comida = db.query(tablaComida).filter(tablaComida.id == id).first()
    if comida is None:
        raise HTTPException(status_code=404, detail=f"No se ha podido encontrar una comida con ID: {id}.")
    
    db.delete(comida)
    db.commit()
    
    return {"mensaje": "La comida se ha eliminado correctamente."}
