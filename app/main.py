from fastapi import FastAPI
from app.database import engine, Base
from app.models.tarea import Tarea

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Task Manager API"
    }