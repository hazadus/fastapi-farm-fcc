"""
Check whether the request is authorised or not.
"""
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from .jwt_handler import decode_jwt


class JwtBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        HTTPBearer.__init__(self, auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await HTTPBearer.__call__(self, request=request)
        if credentials:
            # Check if there's ANY token passed:
            if not credentials.scheme == 'Bearer':
                raise HTTPException(status_code=403, detail='Invalid or expired token.')
            # Now check if the token is valid:
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            # All is OK:
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail='Invalid or expired token.')

    @staticmethod
    def verify_jwt(jwtoken: str) -> bool:
        """
        Returns True if token is successfully decoded and not expired.
        """
        is_token_valid: bool = False
        try:
            payload = decode_jwt(jwtoken)
        except:
            payload = None

        if payload:
            is_token_valid = True

        return is_token_valid
