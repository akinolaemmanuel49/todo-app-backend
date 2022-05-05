from typing import Any, Union
from fastapi import APIRouter, Depends, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from todo.api_v1.config import Config
from todo.api_v1.schemas.user_schema import AccessTokenData, UserCreate, User, Credentials, TokenData
from todo.api_v1.dependencies.database import get_db
from todo.api_v1.database.actions.user_actions import (
    create_user, get_user_by_id, get_user_by_username, authentication_handler)

router = APIRouter(prefix=Config.API_VERSION_STRING, tags=['User'])
security = HTTPBearer(scheme_name='Bearer')


@router.post('/users', tags=['User'])
def create_user_route(user: UserCreate,
                      db: Session = Depends(get_db)):
    """
    API route to create a new user instance
    """
    create_user(db=db, user=user)
    return {'message': 'User created successfully'}


@router.post("/users/login", tags=["User"], response_model=Union[TokenData, dict])
def login_user(credentials: Credentials, db: Session = Depends(get_db)):
    user = get_user_by_username(db=db, username=credentials.username)
    if not user:
        return {"message": "User not found"}
    if not authentication_handler.decode_password(credentials.password, user.hashed_password):
        return {"message": "Invalid password"}
    access_token = authentication_handler.encode_jwt_token(
        username=user.username)
    refresh_token = authentication_handler.encode_jwt_refresh_token(
        username=user.username)
    return {"access_token": access_token, "refresh_token": refresh_token}


@router.get("/users/refresh", tags=["User"], response_model=Union[AccessTokenData, Any])
def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    refresh_token = credentials.credentials
    new_jwt_token = authentication_handler.refresh_jwt_token(refresh_token)
    return {"access_token": new_jwt_token}


@router.get('/users/{user_id}', response_model=User, tags=['User'])
def get_user_route(user_id: int,
                   db: Session = Depends(get_db)):
    """
    API route to get a user instance by id
    """
    return get_user_by_id(db=db, user_id=user_id)


@router.get('/users/{username}', response_model=User, tags=['User'])
def get_user_route_by_username(username: str, db: Session = Depends(get_db)):
    """
    API route to get a user instance by username
    """
    return get_user_by_username(db=db, username=username)
