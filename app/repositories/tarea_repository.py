from sqlalchemy.orm import Session
from app.models.tarea import Tarea
from app.schemas.tarea import TareaCreate, TareaUpdate, EstadoTarea, OrdenTarea
from app.models.usuario import Usuario

def crear_tarea(db: Session, tarea: TareaCreate, usuario_actual: Usuario):
    nueva_tarea = Tarea(
        titulo=tarea.titulo,
        usuario_id=usuario_actual.id
    )
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea

def obtener_tareas(db: Session, usuario_actual: Usuario, page: int, size: int, estado: EstadoTarea | None, buscar: str | None, orden: OrdenTarea):
    query = db.query(Tarea).filter(Tarea.usuario_id == usuario_actual.id)
    
    if estado:
        query = query.filter(Tarea.estado == estado.value)
    
    if buscar: query= query.filter(Tarea.titulo.ilike(f"%{buscar}%"))
    
    if orden == OrdenTarea.asc:
        query = query.order_by(Tarea.created_at.asc())
    else:
        query = query.order_by(Tarea.created_at.desc())
    
    total = query.count()

    tareas = (query.offset((page - 1) * size).limit(size).all())
    
    return {"tareas": tareas, "total": total, "page": page, "size": size, "total_pages": (total + size - 1) // size}

def obtener_tarea(db: Session, tarea_id: int, usuario_actual: Usuario):
    return db.query(Tarea).filter(Tarea.id == tarea_id, Tarea.usuario_id == usuario_actual.id).first()

def actualizar_tarea(db: Session, tarea_id: int, tarea: TareaUpdate, usuario_actual: Usuario):
    tarea_existente = obtener_tarea(db, tarea_id, usuario_actual)
    if not tarea_existente:
        return None
    
    tarea_existente.titulo = tarea.titulo
    tarea_existente.estado = tarea.estado.value
    db.commit()
    db.refresh(tarea_existente)
    return tarea_existente

def eliminar_tarea(db: Session, tarea_id: int, usuario_actual: Usuario):
    tarea_existente = obtener_tarea(db, tarea_id, usuario_actual)
    if not tarea_existente:
        return None
    
    db.delete(tarea_existente)
    db.commit()
    return tarea_existente