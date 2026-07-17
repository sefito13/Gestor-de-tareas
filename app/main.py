from fastapi import FastAPI
from app.routers.tarea import router as tarea_router
from app.routers.usuario import router as usuario_router
from app.routers.auth import router as auth_router

app = FastAPI()

app.include_router(tarea_router)
app.include_router(usuario_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "message": "Task Manager API"
    }