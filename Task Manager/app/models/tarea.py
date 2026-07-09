from sqlalchemy import Column, Integer, String
from app.database import Base

class Tarea(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    estado = Column(String(20), nullable=False, default="Pendiente")