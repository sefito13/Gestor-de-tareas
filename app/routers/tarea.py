from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.dependencies.database import get_db
from app.schemas.tarea import TareaCreate, TareaUpdate, TareaResponse, EstadoTarea, TareaPaginada, OrdenTarea
from app.services import tarea_service
from app.dependencies.auth import obtener_usuario_actual
from app.models.usuario import Usuario
from app.core.exceptions import tarea_no_encontrada

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
    return tarea_service.crear_tarea(db, tarea, usuario_actual)

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
    buscar: str | None = Query(
        default=None,
        description="Buscar por titulo"
    ),
    orden: OrdenTarea = Query(
        default=OrdenTarea.asc,
        description="Orden de creacion"
    ),
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(obtener_usuario_actual)
):
    return tarea_service.obtener_tareas(db, usuario_actual, page, size, estado, buscar, orden)

@router.get("/{tarea_id}", response_model=TareaResponse, status_code=status.HTTP_200_OK)
def obtener_tarea(
    tarea_id: int,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(obtener_usuario_actual)
):
    tarea = tarea_service.obtener_tarea(db, tarea_id, usuario_actual)
    
    if not tarea:
        tarea_no_encontrada()
        
    return tarea


@router.put("/{tarea_id}", response_model=TareaResponse, status_code=status.HTTP_200_OK)
def actualizar_tarea(
    tarea_id: int,
    tarea: TareaUpdate,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(obtener_usuario_actual)
):
    tarea_actualizada = tarea_service.actualizar_tarea(db, tarea_id, tarea, usuario_actual)
    
    if not tarea_actualizada:
        tarea_no_encontrada
    
    return tarea_actualizada

@router.delete("/{tarea_id}", status_code=status.HTTP_200_OK)
def eliminar_tarea(
    tarea_id: int,
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(obtener_usuario_actual)
):
    tarea_existente = tarea_service.eliminar_tarea(db, tarea_id, usuario_actual)
    
    if not tarea_existente:
        tarea_no_encontrada()
    
    return {"message": "Tarea eliminada con exito"}