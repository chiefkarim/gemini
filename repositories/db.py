import asyncpg
import os
from dotenv import load_dotenv


load_dotenv()
POSTGRESQL_HOST = os.getenv("POSTGRESQL_HOST")
POSTGRESQL_DATABASE = os.getenv("POSTGRESQL_DATABASE")
POSTGRESQL_USER = os.getenv("POSTGRESQL_USER")
POSTGRESQL_PASSWORD = os.getenv("POSTGRESQL_PASSWORD")

if not POSTGRESQL_HOST:
    raise ValueError("Please add HOST to .env file!")
if not POSTGRESQL_DATABASE:
    raise ValueError("Please add POSTGRESQL_DATABASE to .env file!")
if not POSTGRESQL_USER:
    raise ValueError("Please add POSTGRESQL_USER to .env file!")
if not POSTGRESQL_PASSWORD:
    raise ValueError("Please add PASSWORD to .env file!")

async def connect_db():
    """Establish a connection to the PostgreSQL database."""
    try:
        conn = await asyncpg.connect(host=POSTGRESQL_HOST,database=POSTGRESQL_DATABASE,user=POSTGRESQL_USER,password=POSTGRESQL_PASSWORD)
        print("successfully connected to posgress database")
        return conn
    except Exception as e:
        raise RuntimeError(f"Database connection faild: {e}")
