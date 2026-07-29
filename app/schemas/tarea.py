from pydantic import BaseModel, Field, field_validator
from enum import Enum
from datetime import datetime

class EstadoTarea(str, Enum):
    pendiente = "Pendiente"
    en_curso = "En Curso"
    completada = "Completada"
    
class  PrioridadTarea(str, Enum):
    alta = "Alta"
    media = "Media"
    baja = "Baja"

class TareaBase(BaseModel):
    titulo: str = Field(
        ..., 
        min_length=3, 
        max_length=100
    )

class TareaCreate(TareaBase):
    prioridad: PrioridadTarea = PrioridadTarea.media
    fecha_vencimiento: datetime | None = None
    @field_validator("titulo")
    @classmethod
    def validar_titulo(cls, value: str):
        value = value.strip()
        
        if not value:
            raise ValueError("El titulo no puede estar vacio")
        return value
    

class TareaUpdate(TareaBase):
    estado: EstadoTarea
    prioridad: PrioridadTarea
    fecha_vencimiento: datetime | None = None
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
    prioridad: PrioridadTarea
    fecha_vencimiento: datetime | None = None
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }

class TareaPaginada(BaseModel):
    items: list[TareaResponse]
    total: int
    page: int
    size: int
    total_pages: int
    
class OrdenTarea(str, Enum):
    asc = "asc"
    desc = "desc"
    
class ResumenTareas(BaseModel):
    total: int
    pendiente: int
    en_curso: int
    completadas: int