from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
import jwt
from app.config import (SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES)

password_hash = PasswordHash.recommended()

def hashear_password(password: str) -> str:
    return password_hash.hash(password)

def verificar_password(
    password_plano: str,
    password_hasheado: str
) -> bool:
    return password_hash.verify(
        password_plano,
        password_hasheado
    )

def crear_acces_token(data: dict) -> str:
    datos_token = data.copy()
    
    expiracion = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    
    datos_token.update({
        "exp": expiracion
    })
    
    token = jwt.encode(
        datos_token,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return token
