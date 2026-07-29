import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.config import SECRET_KEY, ALGORITHM
from app.repositories import usuario_repository
from app.dependencies.database import get_db
from app.core.exceptions import token_invalido

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

def obtener_usuario_actual(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        usuario_id = payload.get("sub")

        if usuario_id is None:
            token_invalido
            
        usuario_id = int(usuario_id)

    except (jwt.InvalidTokenError, ValueError):
        token_invalido

    usuario = usuario_repository.obtener_usuario_por_id(db, usuario_id)

    if usuario is None:
        token_invalido

    return usuario


