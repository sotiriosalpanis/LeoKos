from datetime import timedelta
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
import os

from core.routers.database_client import db
from core.models.user import User, Token
from core.auth.oauth import authenticate_user
from core.auth.hashing import get_password_hash, verify_password
from core.auth.jwt_token import create_access_token, get_current_user

load_dotenv()
access_token_expire = 30

router = APIRouter()


@router.post("/register")
async def create_user(request: User):
    hashed_pwd = get_password_hash(request.password)
    user_object = dict(request)
    user_object['password'] = hashed_pwd
    user_id = await db['users'].insert_one(user_object)
    return {"res" : f'Profile created for {user_object["username"]}'}

@router.post('/token', response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await db['users'].find_one({"username": form_data.username})
    verify = verify_password(form_data.password, user['password'])
    if not user or not verify:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=access_token_expire)
    access_token = create_access_token(
        data= {'sub': user['username']}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type":"bearer"}

@router.get("/users/me", response_model=User)
async def read_user_me(current_user: User = Depends(get_current_user)):
    return current_user
