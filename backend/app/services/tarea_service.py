import math
from sqlalchemy.orm import Session
from app.schemas.tarea import TareaCreate, TareaUpdate, EstadoTarea, TareaPaginada, OrdenTarea
from app.repositories import tarea_repository
from app.models.usuario import Usuario
from datetime import datetime

def crear_tarea(db: Session, tarea: TareaCreate, usuario_actual: Usuario):
    return tarea_repository.crear_tarea(db, tarea, usuario_actual)

def obtener_tareas(db: Session, usuario_actual: Usuario, page:int, size: int, estado: EstadoTarea | None, buscar: str | None, orden: OrdenTarea, desde: datetime | None, hasta: datetime | None):
    tareas, total = tarea_repository.obtener_tareas(db, usuario_actual, page, size, estado, buscar, orden, desde, hasta)
    
    total_pages = max(1, math.ceil(total / size))
    
    return TareaPaginada(items=tareas, total=total, page=page, size=size, total_pages=total_pages)

def obtener_tarea(db: Session, tarea_id: int, usuario_actual: Usuario):
    return tarea_repository.obtener_tarea(db, tarea_id, usuario_actual)

def actualizar_tarea(db: Session, tarea_id: int, tarea: TareaUpdate, usuario_actual: Usuario):
    return tarea_repository.actualizar_tarea(db, tarea_id, tarea, usuario_actual)

def eliminar_tarea(db: Session, tarea_id: int, usuario_actual: Usuario):
    return tarea_repository.eliminar_tarea(db, tarea_id, usuario_actual)

def obtener_resumen(db: Session, usuario_actual: Usuario):
    return tarea_repository.obtener_resumen(db, usuario_actual)