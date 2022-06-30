from dotenv import load_dotenv
from jose import jwt
import os
import time
from typing import Dict





load_dotenv()
secret_key = os.getenv('SECRET_KEY')
algorithm = os.getenv('ALGORITHM')


def token_response(token: str):
    return {
        "access_token" : token
    }

def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, secret_key, algorithm=algorithm)

    return token_response(token)

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, secret_key, algorithms=[algorithm])
        return decoded_token if decoded_token['expires'] >= time.time() else None
    except:
        return {}