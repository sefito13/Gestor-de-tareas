from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.config import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    connect_args= {"check_same_thread": False}
)

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(
    autocommit=False, 
    bind=engine, 
    autoflush=False
)