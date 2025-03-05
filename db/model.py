from sqlalchemy import Column, Float, Integer, String
from db.database import Base

class tablaComida(Base):
    __tablename__= "comida"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable = False)
    paisProcedencia = Column(String, nullable = False)
    numIngredientes = Column(Integer, nullable = False)
    precio = Column(Float, nullable = False)
