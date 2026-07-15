from fastapi import FastAPI
from app.database import engine, Base
from app.routers.tarea_router import router as tarea_router
from app.routers.usuario_router import router as usuario_router
from app.routers.auth_router import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tarea_router)
app.include_router(usuario_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "message": "Task Manager API"
    }