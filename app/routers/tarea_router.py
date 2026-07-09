from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.tarea import Tarea
from app.schemas.tarea import TareaCreate

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