from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate

def crear_usuario(db: Session, usuario: UsuarioCreate) -> Usuario:
    nuevo_usuario = Usuario(
        nombre=usuario.nombre,
        correo=usuario.correo,
        password=usuario.password
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def obtener_usuario_por_correo(db: Session, correo: str) -> Usuario:
    return db.query(Usuario).filter(Usuario.correo == correo).first()