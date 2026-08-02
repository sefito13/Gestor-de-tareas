from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime, UTC
from sqlalchemy.orm import relationship
from app.database import Base

class Tarea(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    estado = Column(String(20), nullable=False, default="Pendiente")
    prioridad = Column(String(20), nullable=False, default="Media")
    fecha_vencimiento = Column(DateTime(timezone=True), nullable=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC), nullable=False)
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC), nullable=False)
    
    usuario = relationship("Usuario", back_populates="tareas")