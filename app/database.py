from sqlmodel import Session,create_engine,SQLModel
from app.config.db_config import get_settings

settings = get_settings()

engine = create_engine("postgresql://postgres:postgres@localhost:5432/rapidfire")

def create_db_and_tables():
    print("Creating database and tables...")
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session