# This file was made by my self not part of the course and was not implemented

import dotenv
import os
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor
import psycopg2

load_dotenv()
db_password = os.getenv("db_password")


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
except Exception as error:
    print("Connecting to database failed")
    print("Error: ", error)
    print(db_password)