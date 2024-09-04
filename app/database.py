from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# This cosde bellow is responsible for connecting the database to the application uing Sql directly
from psycopg2.extras import RealDictCursor
import psycopg2
import time


# Loading the environment variables
load_dotenv()
db_password = os.getenv("DATABASE_PASSWORD")

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{db_password}@localhost/fastapi_course"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"


# The code below is applicable to SQLite databases

# Establish a connection to the database using engine
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Initiating the database session
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()



engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creating a session for talking to the database
sessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

"""
The declarative base class is used to define SQLAlchemy models.
 It provides a way to create database tables that correspond to Python classes. 
 This line creates the base class that all database models will inherit from.
"""
Base = declarative_base()

# This is the first method where SQL commands were excecuted directly
while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="fastapi_course",
            user="postgres",
            password=db_password,
            cursor_factory=RealDictCursor
        )
        # Cursor factory is used to return the data as a dictionary plus the column names

        # Creating a cursor object
        cursor = conn.cursor()
        print("Database connection was successful:!!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)