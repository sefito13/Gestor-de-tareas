from pydantic import BaseModel, Field
from enum import Enum

class EstadoTarea(str, Enum):
    pendiente = "Pendiente"
    en_curso = "En Curso"
    completada = "Completada"

class TareaBase(BaseModel):
    titulo: str = Field(
        ..., 
        min_length=3, 
        max_length=100
    )

class TareaCreate(TareaBase):
    pass

class TareaUpdate(TareaBase):
    estado: EstadoTarea

class TareaResponse(TareaBase):
    id: int
    estado: EstadoTarea

    model_config = {
        "from_attributes": True
    }
