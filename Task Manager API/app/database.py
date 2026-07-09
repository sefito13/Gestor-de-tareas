from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///tareas.db")

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Tarea(Base):
    __tablename__ = "tareas"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100))
    estado = Column(String(20))