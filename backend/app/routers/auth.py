from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.dependencies.database import get_db
from app.services import auth_service
from app.core.security import crear_access_token
from app.core.exceptions import credenciales_invalidas
from app.schemas.auth_schema import LoginRequest

router = APIRouter(
    prefix="/auth", 
    tags=["Autentificación"]
)

@router.post("/login", status_code=status.HTTP_200_OK)
def login(
    datos: LoginRequest,
    db: Session = Depends(get_db)
):
    usuario = auth_service.autenticar_usuario(
        db,
        datos.correo,
        datos.password
    )
    
    if not usuario:
        raise credenciales_invalidas
        
    access_token = crear_access_token(
        data={"sub": str(usuario.id)}
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
