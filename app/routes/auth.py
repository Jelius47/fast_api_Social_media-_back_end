from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi import APIRouter,Depends,HTTPException,status,Response
from sqlalchemy.orm import Session
from . import oath2
from .. import models,utils
from ..database import get_db
from ..schema import UserLogin,Token

router = APIRouter(
    tags=['Authentication']
)

@router.post("/login",response_model=Token)
# On the variable user_credential, we are using the OAuth2PasswordRequestForm 
# class to define the schema of the data that will be sent to the API.
# This data will be saved in the user_credential variable.insted of using the UserLogin schema
def login(user_credential:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # user_credential will returnthe following
    # {
    #     "username": "johndoe",
    #     "password": "secret"
    # }
    # print(user_credential.username)
    # print(user_credential.password)
    # Belollow the line model.Usser.email is equated to user_credential.username because 
    # the OAuth2PasswordRequestForm class has a username attribute that is used to retrieve
    #  the username from the request.
    user = db.query(models.User).filter(models.User.email==user_credential.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Invalid credentials")
    if not utils.verify(user_credential.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Invalid credentials")
    # Create a token
    access_tooken = oath2.create_access_token(data={"user_id":user.id})
    # Return a token
    return {"access_token": access_tooken,"token_type":"Bearer"}
