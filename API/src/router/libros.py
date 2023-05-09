from fastapi import APIRouter, HTTPException
from schemas import LibroResponseModel
from data.datos import retornoDatos
from fastapi import HTTPException

router = APIRouter(
    prefix = "/libros",
    tags = ['libros']
)

@router.get('/')
async def obtener_libros():
    return retornoDatos()


@router.get('/{id}')
async def obtener_libro(id: int):
    lista = retornoDatos()
    if id >= 6:
        raise HTTPException("id inexistente")
    return lista[id - 1]


@router.get('/unidades/{unidades}')
async def obtener_unidades(unidades: float):
    lista = retornoDatos()
    coincidencias = []
    for i in lista:
        if i["unidades"] <= unidades:
            coincidencias.append(i)
    return coincidencias
