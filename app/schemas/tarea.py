from pydantic import BaseModel, Field

class TareaCreate(BaseModel):
    titulo: str = Field(
        ..., 
        min_length=3, 
        max_length=100
    )