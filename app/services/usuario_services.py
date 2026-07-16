from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate
from app.repositories import usuario_repository
from app.core.security import hashear_password

def crear_usuario(db: Session, usuario: UsuarioCreate):
    usuario_existente = usuario_repository.obtener_usuario_por_correo(
        db, usuario.correo
    )

    if usuario_existente:
        raise HTTPException(status_code=409, detail="El correo ya esta registrado")
    
    password_hasheado = hashear_password(usuario.password)
    return usuario_repository.crear_usuario(db, usuario, password_hasheado)

def obtener_usuario_por_correo(db: Session, correo: str):
    return db.query(Usuario).filter(Usuario.correo == correo).first() 
