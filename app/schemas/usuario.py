from pydantic import BaseModel, Field, EmailStr

class UsuarioBase(BaseModel):
    nombre: str = Field(
        ..., 
        min_length=3, 
        max_length=100
    )
    correo: EmailStr 
    password: str = Field(
        ..., 
        min_length=8
    )

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(UsuarioBase):
    pass
    
class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    correo: EmailStr

    model_config = {
        "from_attributes": True
    }
    
class UsuarioLogin(BaseModel):
    correo : EmailStr
    password: str