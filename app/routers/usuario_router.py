from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from app.services import usuario_services
from app.dependencies.auth import obtener_usuario_actual
from app.models.usuario import Usuario

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def crear_usuario(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):
    return usuario_services.crear_usuario(db, usuario)

@router.get("/me", response_model=UsuarioResponse, status_code=status.HTTP_200_OK)
def obtener_mi_perfil(
    usuario_actual: Usuario = Depends(obtener_usuario_actual)
):
    return usuario_actual