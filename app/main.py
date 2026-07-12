from fastapi import FastAPI
from app.database import engine, Base
from app.models.tarea import Tarea
from app.routers.tarea_router import router as tarea_router
from app.models.usuario import Usuario
from app.routers.usuario_router import router as usuario_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tarea_router)
app.include_router(usuario_router)

@app.get("/")
def root():
    return {
        "message": "Task Manager API"
    }