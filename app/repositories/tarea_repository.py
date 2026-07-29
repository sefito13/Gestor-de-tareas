from sqlalchemy.orm import Session
from app.models.tarea import Tarea
from app.schemas.tarea import TareaCreate, TareaUpdate, EstadoTarea, OrdenTarea
from app.models.usuario import Usuario
from datetime import datetime

def crear_tarea(db: Session, tarea: TareaCreate, usuario_actual: Usuario):
    nueva_tarea = Tarea(
        titulo=tarea.titulo,
        usuario_id=usuario_actual.id,
        prioridad=tarea.prioridad.value,
        fecha_vencimiento=tarea.fecha_vencimiento
    )
    db.add(nueva_tarea)
    
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea

def obtener_tareas(db: Session, usuario_actual: Usuario, page: int, size: int, estado: EstadoTarea | None, buscar: str | None, orden: OrdenTarea, desde: datetime | None, hasta: datetime | None):
    query = db.query(Tarea).filter(Tarea.usuario_id == usuario_actual.id)
    
    if estado:
        query = query.filter(Tarea.estado == estado.value)
    
    if buscar:
        query = query.filter(Tarea.titulo.ilike(f"%{buscar}%"))
    
    if desde:
        query = query.filter(Tarea.created_at >= desde)
    
    if hasta:
        query = query.filter(Tarea.created_at <= hasta)
    
    if orden == OrdenTarea.asc:
        query = query.order_by(Tarea.created_at.asc())
    else:
        query = query.order_by(Tarea.created_at.desc())
    
    total = query.count()

    tareas = (query.offset((page - 1) * size).limit(size).all())
    
    return tareas, total

def obtener_tarea(db: Session, tarea_id: int, usuario_actual: Usuario):
    return db.query(Tarea).filter(Tarea.id == tarea_id, Tarea.usuario_id == usuario_actual.id).first()

def actualizar_tarea(db: Session, tarea_id: int, tarea: TareaUpdate, usuario_actual: Usuario):
    tarea_existente = obtener_tarea(db, tarea_id, usuario_actual)
    if not tarea_existente:
        return None
    
    tarea_existente.titulo = tarea.titulo
    tarea_existente.estado = tarea.estado.value
    tarea_existente.prioridad = tarea.prioridad.value
    tarea_existente.fecha_vencimiento = tarea.fecha_vencimiento
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

def obtener_resumen(db: Session, usuario_actual: Usuario):
    query = db.query(Tarea).filter(Tarea.usuario_id == usuario_actual.id)

    total = query.count()

    pendientes = query.filter(
        Tarea.estado == EstadoTarea.pendiente.value
    ).count()

    en_curso = query.filter(
        Tarea.estado == EstadoTarea.en_curso.value
    ).count()

    completadas = query.filter(
        Tarea.estado == EstadoTarea.completada.value
    ).count()

    return {
        "total": total,
        "pendientes": pendientes,
        "en_curso": en_curso,
        "completadas": completadas
    }