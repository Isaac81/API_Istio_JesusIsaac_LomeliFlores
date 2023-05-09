from pydantic import BaseModel


class LibroResponseModel(BaseModel):
    id: int
    titulo: str
    autor: str
    precio: float
    unidades: int