from fastapi import HTTPException, status

def tarea_no_encontrada():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Tarea no encontrada"
    )
    
def usuario_no_encontrado():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado"
    )
    
def correo_ya_registrado():
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="El correo ya esta registrado"
    )
    
def credenciales_invalidas():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Correo o contraseña incorrectos",
        headers={"WWW-Authenticate": "Bearer"}
    )
    
def token_invalido():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"}
    )