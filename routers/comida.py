from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/comida",
                   tags=["comida"],
                   responses={404: {"mensaje": "No se han encontrado resultados."}})

class Comida(BaseModel):
    id: int
    nombre: str
    paisProcedencia: str
    numIngredientes: int
    precio: float

listaComidas = [Comida(id=1, nombre="Tortilla de patatas", paisProcedencia="España", numIngredientes=5, precio=9.20),
                Comida(id=2, nombre="Rabo de toro", paisProcedencia="España", numIngredientes=16, precio=15.10),
                Comida(id=3, nombre="Bouneschlupp", paisProcedencia="Luxemburgo", numIngredientes=12, precio=19.99),
                Comida(id=4, nombre="Fish & chips", paisProcedencia="Reino Unido", numIngredientes=12, precio=7.67),
                Comida(id=5, nombre="Schnitzel Holstein", paisProcedencia="Alemania", numIngredientes=7, precio=17.50)]

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

    if type(buscarComidaPorID(comida.id)) == Comida:
        raise HTTPException(status_code=404, detail=f"Ya existe una comida con ID: {comida.id}.")

    listaComidas.append(comida)
    return comida

# edit
@router.put("/")
async def edit(comida: Comida):
    encontrado = False

    for i, elemento in enumerate(listaComidas):
        if elemento.id == comida.id:
            listaComidas[i] = comida
            encontrado = True

    if not encontrado:
        return {"error": "No se ha podido editar la comida."}
    return comida

# delete
@router.delete("/{id}")
async def delete(id: int):
    encontrado = False

    for i, elemento in enumerate(listaComidas):
        if elemento.id == id:
            del listaComidas[i]
            encontrado = True
        return {"mensaje": "La comida se ha eliminado correctamente."}

    if not encontrado:
        return {"error": "No se ha podido eliminar la comida"}

# MÉTODOS DE SERVICIO -----------------------------------------------------------------------------

def buscarComidaPorID(id: int):
    comidaFiltrada = filter(lambda comida: comida.id == id, listaComidas)
    try:
        return list(comidaFiltrada)[0]
    except:
        return {"error": f"No se ha encontrado ninguna comida con ID: {id}."}
