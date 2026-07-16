from pydantic import BaseModel, Field, field_validator
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
    @field_validator("titulo")
    @classmethod
    def validar_titulo(cls, value: str):
        value = value.strip()
        
        if not value:
            raise ValueError("El titulo no puede estar vacio")
        return value
    

class TareaUpdate(TareaBase):
    estado: EstadoTarea

    @field_validator("titulo")
    @classmethod
    def validar_titulo(cls, value: str):
        value = value.strip()
        
        if not value:
            raise ValueError("El titulo no puede estar vacio")
        return value
class TareaResponse(TareaBase):
    id: int
    estado: EstadoTarea

    model_config = {
        "from_attributes": True
    }

class TareaPaginada(BaseModel):
    items: list[TareaResponse]
    total: int
    page: int
    size: int
    total_pages: int