from sqlalchemy.orm import Session
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate
from app.repositories import usuario_repository

def crear_usuario(db: Session, usuario: UsuarioCreate):
    return usuario_repository.crear_usuario(db, usuario)

def obterner_usuario_por_correo(db: Session, correo: str):
    return usuario_repository.obtener_usuario_por_correo(db, correo)