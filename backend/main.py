from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.tarea import router as tarea_router
from app.routers.usuario import router as usuario_router
from app.routers.auth import router as auth_router

app = FastAPI(
    title="Task Manager API",
    description="API para gestion de tareas",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print(">>> Este es mi main <<<")

app.include_router(tarea_router)
app.include_router(usuario_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "message": "Task Manager API"
    }
