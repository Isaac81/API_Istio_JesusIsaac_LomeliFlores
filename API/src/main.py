from fastapi import FastAPI
from router import libros

app = FastAPI(
    title='API-Kubernetes',
    description='API para materia tolerante a fallas',
    version='1.0.0'
)

app.include_router(libros.router)

@app.on_event("startup")
def startup():
    print("Iniciando servidor")


@app.on_event("shutdown")
def shutdown():
    print("Cerrando servidor")


@app.get('/')
async def root():
    return { 'root' : 'hola' }