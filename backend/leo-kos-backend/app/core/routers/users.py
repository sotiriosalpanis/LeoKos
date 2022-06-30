from dotenv import load_dotenv
from fastapi import APIRouter, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from jose import JWTError, jwt
import os
from passlib.context import CryptContext
from typing import Union


from core.routers.database_client import db
from core.models.database import UserSchema, UserLoginSchema
from core.auth.auth_handler import signJWT

load_dotenv()
secret_key = os.getenv('SECRET_KEY')
algorithm = os.getenv('ALGORITHM')
access_token_expire = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')

router = APIRouter()
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_password_hash(password):
    return pwd_context.hash(password)

# def check_user(data: UserLoginSchema):
#     for user in users:
#         if user.username == data.email and user.password == data.password:
#             return True
#     return False

@router.post("/register")
async def create_user(user: UserSchema = Body(...)):
    hashed_password = get_password_hash(user.password)
    user.password = hashed_password
    user = jsonable_encoder(user)
    new_user = await db['users'].insert_one(user)
    created_user = await db['users'].find_one({"_id": new_user.inserted_id})
    if created_user:
        return signJWT(user.username)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return credentials_exception

@router.post("/login")
async def user_login(user: UserLoginSchema = Body(...)):
    try:
        user_in_db = await db['users'].find_one({"username": user.username})
        print('USER IN DB: ', user_in_db)
    
    except JWTError:
        credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
        )
        raise credentials_exception


# pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def get_password_hash(password):
#     return pwd_context.hash(password)

# async def get_user(db, username: str):
#     print('2. Get user')
#     if (user := await db['users'].find_one({"username": username})) is not None:
#         print('User:', user)
#         return user
#     print('NO dice')


# def authenticate_user(db, username: str, password: str):
#     print('1. Authenticate user')
#     user = get_user(db, username)
#     if not user: 
#         return False
#     if not verify_password(password, user.password):
#         return False
#     return user

# def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({'exp':expire})
#     encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
#     return encoded_jwt

# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, secret_key, algorithms=[algorithm])
#         username: str = payload.get('sub')
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#     user = get_user(db, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user

# @router.post("/token")
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="incorrect username or password",
#         headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=access_token_expire)
#     access_token = create_access_token(
#         data={'sub': user.username}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type":"bearer"}

# @router.get('/me')
# async def read_users_me(current_user: User = Depends(get_current_user)):
#     return current_user

# @router.post("/register")
# async def create_user(user: UserInDB):
#     hashed_password = get_password_hash(user.password)
#     user.password = hashed_password
#     user = jsonable_encoder(user)
#     new_user = await db['users'].insert_one(user)
#     created_user = await db['users'].find_one({"_id": new_user.inserted_id})
#     msg = f'User created for {created_user.username}'
#     return JSONResponse(status_code = status.HTTP_201_CREATED, content=msg)
