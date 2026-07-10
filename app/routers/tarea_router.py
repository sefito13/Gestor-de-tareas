from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.tarea import Tarea
from app.schemas.tarea import TareaCreate, TareaUpdate

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/tareas",
    tags=["tareas"]
)

@router.post("/")
def crear_tarea(
    tarea: TareaCreate,
    db: Session = Depends(get_db)
):
    nueva_tarea = Tarea(
        titulo=tarea.titulo
    )

    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    
    return nueva_tarea

@router.get("/")
def obtener_tareas(
    db: Session = Depends(get_db)
):
    tareas = db.query(Tarea).all()
    return tareas

@router.get("/{tarea_id}")
def obtener_tarea(
    tarea_id: int,
    db: Session = Depends(get_db)
):
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if not tarea:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )
    
    return tarea

@router.put("/{tarea_id}")
def actualizar_tarea(
    tarea_id:int,
    tarea: TareaUpdate,
    db: Session = Depends(get_db)
):
    tarea_existente = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if not tarea_existente:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )
    
    tarea_existente.titulo = tarea.titulo
    tarea_existente.estado = tarea.estado.value

    db.commit()
    db.refresh(tarea_existente)

    return tarea_existente

@router.delete("/{tarea_id}")
def eliminar_tarea(
    tarea_id: int,
    db: Session = Depends(get_db)
):
    tarea_existente = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if not tarea_existente:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )
    
    db.delete(tarea_existente)
    db.commit()

    return {"message": "Tarea eliminada con exito"}