from sqlalchemy.orm import Session
from app.repositories import usuario_repository
from app.core.security import verificar_password

def autenticar_usuario(db:Session, correo: str, password: str):
    usuario = usuario_repository.obtener_usuario_por_correo(db, correo)
    
    if not usuario:
        return None
    
    if not verificar_password(password, usuario.password):
        return None
    
    return usuario