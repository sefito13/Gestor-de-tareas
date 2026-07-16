from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.tarea import TareaCreate, TareaUpdate, TareaResponse
from app.services import tarea_services
from app.dependencies.auth import obtener_usuario_actual
from app.models.usuario import Usuario

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

@router.post("/", response_model=TareaResponse)
def crear_tarea(
    tarea: TareaCreate,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(obtener_usuario_actual)
):
    return tarea_services.crear_tarea(db, tarea, usuario_actual)

@router.get("/", response_model=list[TareaResponse])
def obtener_tareas(
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(obtener_usuario_actual)
):
    return tarea_services.obtener_tareas(db, usuario_actual)

@router.get("/{tarea_id}", response_model=TareaResponse)
def obtener_tarea(
    tarea_id: int,
    db: Session = Depends(get_db)
):
    tarea = tarea_services.obtener_tarea(db, tarea_id)
    if not tarea:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )
    return tarea


@router.put("/{tarea_id}", response_model=TareaResponse)
def actualizar_tarea(
    tarea_id: int,
    tarea: TareaUpdate,
    db: Session = Depends(get_db)
):
    tarea_existente = tarea_services.obtener_tarea(db, tarea_id)
    if not tarea_existente:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )
    
    return tarea_services.actualizar_tarea(db, tarea_id, tarea)

@router.delete("/{tarea_id}")
def eliminar_tarea(
    tarea_id: int,
    db: Session = Depends(get_db)
):
    tarea_existente = tarea_services.eliminar_tarea(db, tarea_id)
    if not tarea_existente:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )
    
    return {"message": "Tarea eliminada con exito"}