from fastapi import FastAPI,Depends,Response,status,HTTPException,APIRouter

# For the pydantic schema
from ..schema import *


# Database 
from ..database import engine,get_db
from .. import models,utils
from sqlalchemy.orm import Session  


router = APIRouter(
    prefix="/users",
    tags=['Users']
)



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Hash the password
    # hashed_password = pwd_context.hash(user.password)

    # Hashing the password 
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    # Create a new user object
    new_user = models.User(**user.model_dump(),)
    
    # Add the new user to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@router.get('/{id}',response_model=UserOut)

def get_user(id: int,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id: {id} was not found !!")
    return user
