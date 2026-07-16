from fastapi import APIRouter, Depends, HTTPException
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

@router.post("/", response_model=UsuarioResponse)
def crear_usuario(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):
    usuario_existente = usuario_services.obterner_usuario_por_correo(db, usuario.correo)
    if usuario_existente:
        raise HTTPException(
            status_code=400,
            detail="El correo ya esta registrado"
        )
    return usuario_services.crear_usuario(db, usuario)

@router.get("/me", response_model=UsuarioResponse)
def obtener_mi_perfil(
    usuario_actual: Usuario = Depends(obtener_usuario_actual)
):
    return usuario_actual