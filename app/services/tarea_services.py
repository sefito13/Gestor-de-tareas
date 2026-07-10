from sqlalchemy.orm import Session
from app.models.tarea import Tarea
from app.schemas.tarea import TareaCreate, TareaUpdate

def crear_tarea(db: Session, tarea: TareaCreate):
    nueva_tarea = Tarea(
        titulo=tarea.titulo
    )

    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)

    return nueva_tarea

def obtener_tareas(db: Session):
    return db.query(Tarea).all()

def obtener_tarea(db: Session, tarea_id: int):
    return db.query(Tarea).filter(Tarea.id == tarea_id).first()

def actualizar_tarea(db: Session, tarea_id: int, tarea: TareaUpdate):
    tarea_existente = obtener_tarea(db, tarea_id)
    if not tarea_existente:
        return None
    
    tarea_existente.titulo = tarea.titulo
    tarea_existente.estado = tarea.estado
    db.commit()
    db.refresh(tarea_existente)
    return tarea_existente

def eliminar_tarea(db: Session, tarea_id: int):
    tarea_existente = obtener_tarea(db, tarea_id)
    if not tarea_existente:
        return None
    
    db.delete(tarea_existente)
    db.commit()
    return tarea_existente