from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import Config

Base = declarative_base()
engine = None
SessionLocal = None

def init_db():
    global engine, SessionLocal
    config = Config()
    engine = create_engine(config.database_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
