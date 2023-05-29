import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    URL.create(
        "postgresql",
        username="postgres",
        password="postgres",
        host="dg-database",
        port=5432,
        database="dg_database",
    )
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
