import jwt
from datetime import datetime
from typing import Optional

from passlib.context import CryptContext
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder

from todo.api_v1.config import Config
from todo.api_v1.schemas.error_response_schema import ErrorResponse


class Authentication:
    pwd_context = CryptContext(Config.ENCRYPTION_SCHEMES)
    jwt_secret_key = Config.JWT_SECRET_KEY

    def encode_password(self, plain_password: str) -> Optional[str]:
        return self.pwd_context.hash(plain_password)

    def decode_password(self, plain_password: str, encoded_password: Optional[str]) -> bool:
        return self.pwd_context.verify(plain_password, encoded_password)

    def encode_jwt_token(self, username: str) -> str:
        payload = {
            'exp': datetime.utcnow() + Config.JWT_ACCESS_TOKEN_EXPIRES,
            'iat': datetime.utcnow(),
            'sub': username
        }
        return jwt.encode(payload, self.jwt_secret_key, algorithm=Config.JWT_ALGORITHM)

    def decode_jwt_token(self, token: str) -> Optional[str]:
        try:
            payload = jwt.decode(token, self.jwt_secret_key,
                                 algorithms=Config.JWT_ALGORITHM)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail=jsonable_encoder(ErrorResponse(
                message="Token has expired", code=status.HTTP_401_UNAUTHORIZED)))
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=jsonable_encoder(ErrorResponse(
                message='Invalid token', code=status.HTTP_401_UNAUTHORIZED)))

    def encode_jwt_refresh_token(self, username: str) -> Optional[str]:
        payload = {
            'exp': datetime.utcnow() + Config.JWT_REFRESH_TOKEN_EXPIRES,
            'iat': datetime.utcnow(),
            'sub': username
        }
        return jwt.encode(payload, self.jwt_secret_key, Config.JWT_ALGORITHM)

    def refresh_jwt_token(self, jwt_refresh_token: str) -> Optional[str]:
        try:
            payload = jwt.decode(
                jwt_refresh_token, self.jwt_secret_key, Config.JWT_ALGORITHM)
            username = payload['sub']
            new_jwt_token = self.encode_jwt_token(username)
            return new_jwt_token
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail=jsonable_encoder(ErrorResponse(
                message="Token has expired", code=status.HTTP_401_UNAUTHORIZED)))
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=jsonable_encoder(ErrorResponse(
                message='Invalid token', code=status.HTTP_401_UNAUTHORIZED)))
