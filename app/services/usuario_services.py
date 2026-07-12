from sqlalchemy.orm import Session
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate
from app.repositories import usuario_repository
from app.core.security import hashear_password

def crear_usuario(db: Session, usuario: UsuarioCreate):
    password_hasheado = hashear_password(usuario.password)
    return usuario_repository.crear_usuario(
        db, 
        usuario, 
        password_hasheado
    )

def obterner_usuario_por_correo(db: Session, correo: str):
    return usuario_repository.obtener_usuario_por_correo(db, correo)