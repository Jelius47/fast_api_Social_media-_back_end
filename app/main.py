from fastapi import FastAPI,Depends,Response,status,HTTPException
from random import randrange
from typing import Optional,List



# from db import *

# For the databse connection
import os
from dotenv import load_dotenv

from .routes import post,users,auth,votes

# # For the pydantic schema
# from .schema import *

# # Database 
from .database import engine,get_db
from . import models
# from sqlalchemy.orm import Session 



# This code is the one responsible for creating tables

"""The code below was responsible for creating the tables(using sql alchemy) but due to the 
alembic package it is no longer required 
"""
# models.Base.metadata.create_all(bind=engine) 

# LOading the environment variables
load_dotenv()
db_password = os.getenv("db_password")




"""
Initializes the FastAPI application instance.

This line creates a new FastAPI application instance,
 which is the main entry point for the web application. 
 The FastAPI application is responsible for handling incoming HTTP requests,
 routing them to the appropriate handlers, and managing the application's lifecycle.
"""
app = FastAPI()

app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)



# Importing CORS intergration for managing our APIs across multiple domains
from fastapi.middleware.cors import CORSMiddleware


origins = ['https://google.com','*']
""" The star will allow all of the domains to talk to
 our APIs"""

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # what domians do we want to talk to with our APIs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Creating a list to store the data for simulating the Database
# hard coding NOT a good practice 
my_post = [
            {
            "title":"title of post 1",
            "content":"content of post 1",
            "id":1,},
            {
            "Favourite food":"Pizza",
            "content":"It just happened but not really my favourite",
            "id":2
            }
            ]
def find_post(id):
    for p in my_post:
        if p["id"] == id:   
            return p
        
def find_post_indx(id):
    for i,p in enumerate(my_post):
        if p["id"] == id:
            return i


# The other route so as to avoid the codding conflict this is for testing purpose
# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return{"data":f"The posts\n {posts}"}







# The async keyword is used to define an asynchronous function.
# The await keyword is used to pause the execution of an asynchronous function until a promise is resolved.
# The asyncio module is used to run asynchronous functions.
# The asyncio.run() function is used to run the main() function.

# pydamtic for defining our schema

