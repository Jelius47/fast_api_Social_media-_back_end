import os
from dotenv import load_dotenv
from datetime import datetime,timedelta,timezone
from jose import JWTError, jwt

from .. import schema,database,models
from sqlalchemy.orm import Session
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer

# test = jwt.encode({"test":"test"},"secret",algorithm="HS256")
# print(test)

oauth_scheme = OAuth2PasswordBearer(tokenUrl = "login")
load_dotenv()
SECRETE_KEY = os.getenv("SECRETE_KEY")
ALGORITHM = os.getenv("ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

def create_access_token(data: dict):
    to_encode = data.copy()
    print(to_encode)
    expire_time = datetime.now(timezone.utc) + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp":expire_time})

    encode_jwt = jwt.encode(to_encode,f"{SECRETE_KEY}",algorithm=ALGORITHM)
    
    return encode_jwt


def verrify_access_token(token: str,credentials_exception):
    try:
        payload = jwt.decode(token,f"{SECRETE_KEY}",algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = schema.TokenData(id=str(id))
    except JWTError:
        raise credentials_exception
    return token_data
    
def get_current_user(token: str= Depends(oauth_scheme),db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Could not validate credentials",
                                          headers={"WWW-Authenticate": "Bearer"})
    token =verrify_access_token(token,credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user