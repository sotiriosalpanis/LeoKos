
from core.models.user import UserInDB
from core.auth.hashing import verify_password

async def get_user(db, username:str):
    print('get user')
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(db, username: str, password: str):
    print('OAUTH',db, username)
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

