"""
Sign, encode, decode, return JWTs.
"""
import time

import jwt
from decouple import config

JWT_SECRET = config('secret')
JWT_ALGORITHM = config('algorithm')


def token_response(token: str):
    """
    Returns generated JWTs used to authenticate in API.
    """
    return {
        'access token': token
    }


def sign_jwt(user_id: str):
    """
    Return signed JWT string.
    """
    payload = {
        'user_id': user_id,
        'expires': time.time() + 3600  # in seconds
    }
    token = jwt.encode(payload=payload, key=JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decode_jwt(encoded_token: str) -> dict:
    """
    Return decoded token, if correct and not expired.
    """
    try:
        decoded_token = jwt.decode(jwt=encoded_token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token['expires'] >= time.time() else None
    except:
        return {}
