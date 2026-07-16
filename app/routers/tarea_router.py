from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.tarea import TareaCreate, TareaUpdate, TareaResponse, EstadoTarea, TareaPaginada
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

@router.post("/", response_model=TareaResponse, status_code=status.HTTP_201_CREATED)
def crear_tarea(
    tarea: TareaCreate,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(obtener_usuario_actual)
):
    return tarea_services.crear_tarea(db, tarea, usuario_actual)

@router.get("/", response_model=TareaPaginada, status_code=status.HTTP_200_OK)
def obtener_tareas(
    page: int = Query(
        default=1,
        ge=1,
        description="Numero de pagina"
    ),
    size: int = Query(
        default=10,
        ge=1,
        le=100,
        description="Cantidad de registros por pagina"
    ),
    estado: EstadoTarea | None = Query(
        default=None,
        description="Filtrar por estado"
    ),
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(obtener_usuario_actual)
):
    return tarea_services.obtener_tareas(db, usuario_actual, page, size, estado)

@router.get("/{tarea_id}", response_model=TareaResponse, status_code=status.HTTP_200_OK)
def obtener_tarea(
    tarea_id: int,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(obtener_usuario_actual)
):
    tarea = tarea_services.obtener_tarea(db, tarea_id, usuario_actual)
    if not tarea:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )
    return tarea


@router.put("/{tarea_id}", response_model=TareaResponse, status_code=status.HTTP_200_OK)
def actualizar_tarea(
    tarea_id: int,
    tarea: TareaUpdate,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(obtener_usuario_actual)
):
    tarea_actualizada = tarea_services.actualizar_tarea(db, tarea_id, tarea, usuario_actual)
    
    if not tarea_actualizada:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )
    
    return tarea_actualizada

@router.delete("/{tarea_id}", status_code=status.HTTP_200_OK)
def eliminar_tarea(
    tarea_id: int,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(obtener_usuario_actual)
):
    tarea_existente = tarea_services.eliminar_tarea(db, tarea_id, usuario_actual)
    if not tarea_existente:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )
    
    return {"message": "Tarea eliminada con exito"}