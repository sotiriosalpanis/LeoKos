from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from dotenv import load_dotenv
from jose import JWTError, jwt
import os
from typing import Union

from core.models.user import TokenData
from core.auth.oauth import get_user
from core.routers.database_client import db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

load_dotenv()
secret_key = os.getenv('SECRET_KEY')
algorithm = os.getenv('ALGORITHM')
access_token_expire = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')

def create_access_token(data: dict, expires_delta: Union[timedelta, None]):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    print(expire)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, secret_key,algorithm=algorithm)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try: 
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user   