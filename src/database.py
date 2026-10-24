
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("La variable DATABASE_URL est absente du fichier .env")

engine = create_engine(DATABASE_URL)


def test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Connexion réussie :", result.scalar())


if __name__ == "__main__":
    test_connection()
