from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from todo.api_v1.config import Config
from todo.api_v1.schemas.user_schema import UserCreate, User
from todo.api_v1.dependencies.database import get_db
from todo.api_v1.database.actions.user_actions import (
    create_user, get_user_by_id)

router = APIRouter(prefix=Config.API_VERSION_STRING, tags=['User'])


@router.post('/users', tags=['User'])
def create_user_route(user: UserCreate,
                      db: Session = Depends(get_db)):
    create_user(db=db, user=user)
    return {'message': 'User created successfully'}


@router.get('/users/{user_id}', response_model=User, tags=['User'])
def get_user_route(user_id: int,
                   db: Session = Depends(get_db)):
    return get_user_by_id(db=db, user_id=user_id)
