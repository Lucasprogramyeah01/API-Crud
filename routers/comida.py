from typing import Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/comida",
                   tags=["comida"],
                   responses={404: {"mensaje": "No se han encontrado resultados."}})

class Comida(BaseModel):
    id: Optional[int] = None    # El ID puede ser None, ya que no se introduce en el "Request body".
    nombre: str
    paisProcedencia: str
    numIngredientes: int
    precio: float

listaComidas = [
    Comida(id=1, nombre="Tortilla de patatas", paisProcedencia="España", numIngredientes=5, precio=9.20),
    Comida(id=2, nombre="Rabo de toro", paisProcedencia="España", numIngredientes=16, precio=15.10),
    Comida(id=3, nombre="Bouneschlupp", paisProcedencia="Luxemburgo", numIngredientes=12, precio=19.99),
    Comida(id=4, nombre="Fish & chips", paisProcedencia="Reino Unido", numIngredientes=12, precio=7.67),
    Comida(id=5, nombre="Schnitzel Holstein", paisProcedencia="Alemania", numIngredientes=7, precio=17.50),
    Comida(id=6, nombre="Ceviche", paisProcedencia="Perú", numIngredientes=6, precio=14.30),
    Comida(id=7, nombre="Kimchi", paisProcedencia="Corea del Sur", numIngredientes=8, precio=5.99),
    Comida(id=8, nombre="Pad Thai", paisProcedencia="Tailandia", numIngredientes=10, precio=13.45),
    Comida(id=9, nombre="Moussaka", paisProcedencia="Grecia", numIngredientes=9, precio=12.80),
    Comida(id=10, nombre="Goulash", paisProcedencia="Hungría", numIngredientes=11, precio=18.75),
    Comida(id=11, nombre="Poutine", paisProcedencia="Canadá", numIngredientes=4, precio=8.50),
    Comida(id=12, nombre="Paella", paisProcedencia="España", numIngredientes=15, precio=21.00),
    Comida(id=13, nombre="Sushi", paisProcedencia="Japón", numIngredientes=6, precio=22.50),
    Comida(id=14, nombre="Borscht", paisProcedencia="Ucrania", numIngredientes=7, precio=10.90),
    Comida(id=15, nombre="Feijoada", paisProcedencia="Brasil", numIngredientes=13, precio=16.60)
]

# findAll
@router.get("/")
async def findAll():
    return listaComidas

# findByID
@router.get("/{id}")
async def findByID(id: int):
    return buscarComidaPorID(id)

# save
@router.post("/", response_model=Comida, status_code=201)
async def save(comida: Comida):
    comida.id = max([c.id for c in listaComidas], default=0) + 1

    if any(c.nombre == comida.nombre for c in listaComidas):
        raise HTTPException(status_code=409, detail=f"No se ha podido agregar la comida, ya existe una con nombre: {comida.nombre}.")

    listaComidas.append(comida)
    return comida

# edit
@router.put("/{id}")
async def edit(id: int, comida: Comida):

    if any(c.nombre == comida.nombre for c in listaComidas):
        return HTTPException(status_code=409, detail=f"No se ha podido editar la comida, ya existe una con nombre: {comida.nombre}.")
    else:
        comidaDeLista = buscarComidaPorID(id)
        comidaDeLista.nombre = comida.nombre
        comidaDeLista.paisProcedencia = comida.paisProcedencia
        comidaDeLista.numIngredientes = comida.numIngredientes
        comidaDeLista.precio = comida.precio

        return comidaDeLista

# delete
@router.delete("/{id}", status_code=204)
async def delete(id: int):
    for i, elemento in enumerate(listaComidas):
        if elemento.id == id:
            del listaComidas[i]

# MÉTODOS DE SERVICIO -----------------------------------------------------------------------------

def buscarComidaPorID(id: int):
    for comida in listaComidas:
        if comida.id == id:
            return comida
    raise HTTPException(status_code=404, detail=f"Ya existe una comida con ID: {comida.id}.")
