from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal

class Tarea(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=100)
    estado: Literal[
        "Pendiente",
        "Completada"
        "En Curso"
    ] = "Pendiente"

app = FastAPI()

@app.get("/saludo/{nombre}")
async def saludo(nombre: str):
    return {"message": f"Hello {nombre}!"}

@app.get("/suma/{num1}/{num2}")
async def suma(num1: int, num2: int):
    return {"resultado": num1 + num2}

@app.get("/saludo")
async def saludo(nombre: str = "Sebastian"):
    return({"message": f"Hello {nombre}!"})


@app.get("/suma")
async def suma(num1: int = 10, num2: int = 5):
    return {"resultado": num1 + num2}

@app.post("/tarea")
async def crear_tarea(tarea: Tarea):
    return tarea