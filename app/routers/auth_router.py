from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.usuario import UsuarioLogin
from app.services import auth_services
from app.core.security import crear_acces_token


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/auth", tags=["Autentificación"])

@router.post("/login")
def login(
    datos: UsuarioLogin,
    db: Session = Depends(get_db)
):
    usuario = auth_services.autenticar_usuario(
        db,
        datos.correo,
        datos.password
    )
    
    if not usuario:
        raise HTTPException(
            status_code=401,
            detail="Correo o contraseña incorrectos"
        )
        
    acces_token = crear_acces_token(
        data={"sub": str(usuario.id)}
    )
    
    return {
        "access_token": acces_token,
        "token_type": "bearer"
    }

