import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

# On récupère l'URL Postgres du .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Création du moteur
# Note : PostgreSQL n'a pas besoin de l'argument 'check_same_thread' de SQLite
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
