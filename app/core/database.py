from sqlmodel import SQLModel, Session, create_engine
from app.core.config import Settings

# create database engine
engine = create_engine(
    Settings.DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread" : False}
)

def create_db_and_tables():
    """Create all database tables"""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Dependency for Fastapi to get database connection"""
    with Session(engine) as session:
        yield session