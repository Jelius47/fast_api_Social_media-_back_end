from pydantic import BaseModel,EmailStr
from pydantic.types import conint
from datetime import datetime
from typing import Optional


# Creating a class which will utilize pydantic to define the schema of our data.
class PostBase(BaseModel):
    tittle: str
    content: str
    published: bool = True
    # id: Optional[int]
    # rating: Optional[int]
    
class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr 
    created_at: datetime
    """This configuration setting enables the Pydantic 
        model to work with SQLAlchemy
        ORM objects, allowing the model to be used with 
        database-backed data."""
    class Config:
        orm_mode = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True

class PostResponse(BaseModel):
   tittle: str
   content : str
   published: bool
   created_at: datetime
   owner_id: int
   owner: UserOut
   
   class Config:
      orm_mode = True

class UserCreate(BaseModel):
   email: EmailStr
   password: str




class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) #le=1 means less than or equal to 1