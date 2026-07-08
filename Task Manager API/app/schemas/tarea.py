from pydantic import BaseModel, Field
from typing import Literal

class TareaBase(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=100)
    estado: Literal[
        "Pendiente",
        "Completada",
        "En Curso"
    ] = "Pendiente"

class TareaCreate(TareaBase):
    pass

class TareaUpdate(TareaBase):
    titulo: str | None = Field(None, min_length=3, max_length=100)
    estado: Literal[
        "Pendiente", 
        "Completada", 
        "En Curso"
    ] = None
    
class TareaResponse(TareaBase):
    id: int
