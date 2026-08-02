from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.dependencies.database import get_db
from app.schemas.usuario import UsuarioCreate, UsuarioResponse
from app.services import usuario_service
from app.dependencies.auth import obtener_usuario_actual
from app.models.usuario import Usuario

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def crear_usuario(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):
    return usuario_service.crear_usuario(db, usuario)

@router.get("/me", response_model=UsuarioResponse, status_code=status.HTTP_200_OK)
def obtener_mi_perfil(
    usuario_actual: Usuario = Depends(obtener_usuario_actual)
):
    return usuario_actual