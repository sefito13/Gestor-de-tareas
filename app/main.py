from fastapi import FastAPI
from app.routers.tarea import router as tarea_router
from app.routers.usuario import router as usuario_router
from app.routers.auth import router as auth_router

openapi_tags = [
    {
        "name": "Auth", 
        "description": "Autenticacion"
    },
    {
        "name": "Usuarios", 
        "description": "Gestion de usuarios"
    },
    {
        "name": "Tareas", 
        "description": "Gestion de tareas"
    }
]

app = FastAPI(
    title="Task Manager API",
    description="API para gestion de tareas",
    version="1.0.0"
)

app.include_router(tarea_router)
app.include_router(usuario_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "message": "Task Manager API"
    }