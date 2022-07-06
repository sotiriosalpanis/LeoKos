from typing import Union
from pydantic import BaseModel, Field

# User Models
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(Token):
    username: Union[str, None] = None

class User(BaseModel):
    username: str = Field(...)
    password: str = Field(...)


class UserInDB(User):
    hashed_password: str

