from sqlalchemy.orm import Session
from app.schemas.tarea import TareaCreate, TareaUpdate
from app.repositories import tarea_repository
from app.models.usuario import Usuario

def crear_tarea(db: Session, tarea: TareaCreate, usuario_actual: Usuario):
    return tarea_repository.crear_tarea(db, tarea, usuario_actual)

def obtener_tareas(db: Session, usuario_actual: Usuario):
    return tarea_repository.obtener_tareas(db, usuario_actual)

def obtener_tarea(db: Session, tarea_id: int):
    return tarea_repository.obtener_tarea(db, tarea_id)

def actualizar_tarea(db: Session, tarea_id: int, tarea: TareaUpdate):
    return tarea_repository.actualizar_tarea(db, tarea_id, tarea)

def eliminar_tarea(db: Session, tarea_id: int):
    return tarea_repository.eliminar_tarea(db, tarea_id)