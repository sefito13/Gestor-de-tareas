from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.dependencies.database import get_db
from app.services import auth_service
from app.core.security import crear_access_token

router = APIRouter(
    prefix="/auth", 
    tags=["Autentificación"]
)

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    usuario = auth_service.autenticar_usuario(
        db,
        form_data.username,
        form_data.password
    )
    
    if not usuario:
        raise HTTPException(
            status_code=401,
            detail="Correo o contraseña incorrectos"
        )
        
    access_token = crear_access_token(
        data={"sub": str(usuario.id)}
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
