from sqlalchemy.orm import Session
from db.model import tablaComida

def findAll(db: Session):
    return db.query(tablaComida).all()

def findByID(db: Session, id: int):
    return db.query(tablaComida).filter(tablaComida.id == id).first()

def save(db: Session, id: int, nombre: str, paisProcedencia: str, 
    numIngredientes: int, precio: float):
    comida = tablaComida(id=id, name=nombre, paisProcedencia=paisProcedencia, 
        numIngredientes=numIngredientes, precio=precio)
    db.add(comida)
    db.commit()
    db.refresh(comida)
    return comida