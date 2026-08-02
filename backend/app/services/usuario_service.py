from sqlalchemy.orm import Session
from app.schemas.usuario import UsuarioCreate
from app.repositories import usuario_repository
from app.core.security import hashear_password
from app.core.exceptions import correo_ya_registrado

def crear_usuario(db: Session, usuario: UsuarioCreate):
    usuario_existente = usuario_repository.obtener_usuario_por_correo(db, usuario.correo)

    if usuario_existente:
        correo_ya_registrado
    
    password_hasheado = hashear_password(usuario.password)
    return usuario_repository.crear_usuario(db, usuario, password_hasheado)

def obtener_usuario_por_correo(db: Session, correo: str):
    return usuario_repository.obtener_usuario_por_correo(db, correo)
