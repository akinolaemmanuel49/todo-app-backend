from typing import List

from fastapi import APIRouter, Depends, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from todo.api_v1.config import Config
from todo.api_v1.schemas.todo_schema import Todo, TodoCreate
from todo.api_v1.dependencies.database import get_db
from todo.api_v1.database.actions.user_actions import authentication_handler, get_user_by_username
from todo.api_v1.database.actions.todo_actions import (create_todo,
                                                       get_done_state,
                                                       get_user_todo_list,
                                                       toggle_done,
                                                       delete_todo,
                                                       )

router = APIRouter(prefix=Config.API_VERSION_STRING, tags=['Todo'])
security = HTTPBearer(scheme_name='Bearer')


@router.post('/todos', tags=['Todo'])
def create_todo_route(todo: TodoCreate,
                      credentials: HTTPAuthorizationCredentials = Security(
                          security),
                      db: Session = Depends(get_db)) -> dict:
    """
    API route to create a new todo instance
    """
    access_token = credentials.credentials
    user_id = get_user_by_username(
        db=db, username=authentication_handler.decode_jwt_token(access_token)).id
    create_todo(db=db, todo=todo.todo, user_id=user_id)
    return {'message': 'Todo created successfully'}


@router.get('/todos', response_model=List[Todo], tags=['Todo'])
def get_todos_by_user_route(credentials: HTTPAuthorizationCredentials = Security(security), db: Session = Depends(get_db)):
    """
    API route to get all todos instances
    """
    credentials = credentials.credentials
    user_id = get_user_by_username(
        db=db, username=authentication_handler.decode_jwt_token(credentials)).id
    return get_user_todo_list(db=db, user_id=user_id)


# @router.get('/todos/{todo_id}', response_model=Todo, tags=['Todo'])
# def get_todo_route(db: Session = Depends(get_db), todo_id: int = None):
#     """
#     API route to get a todo instance by id
#     """
#     return get_todo(db=db, todo_id=todo_id)


# @router.put('/todos/{todo_id}', tags=['Todo'])
# def update_todo_route(todo_id: int,
#                       todo: TodoUpdate,
#                       db: Session = Depends(get_db)):
#     update_todo(db=db,
#                 todo_id=todo_id,
#                 todo=todo.todo,
#                 done=todo.done)
#     return {'message': 'Todo updated successfully'}


@router.get('/todos/{todo_id}/toggle', tags=['Todo'], response_model=bool)
def toggle_done_route(todo_id: int, credentials: HTTPAuthorizationCredentials = Security(security),
                      db: Session = Depends(get_db)):
    """API route to toggle a todo instance done state"""
    credentials = credentials.credentials
    user_id = get_user_by_username(
        db=db, username=authentication_handler.decode_jwt_token(credentials)).id
    toggle_done(db=db, todo_id=todo_id, user_id=user_id)
    return get_done_state(db=db, todo_id=todo_id, user_id=user_id)


@router.get('/todos/{todo_id}/state', tags=['Todo'], response_model=bool)
def get_todo_done_state_route(todo_id: int, credentials: HTTPAuthorizationCredentials = Security(security),
                              db: Session = Depends(get_db)):
    """API route to get a todo instance done state"""
    credentials = credentials.credentials
    user_id = get_user_by_username(
        db=db, username=authentication_handler.decode_jwt_token(credentials)).id
    return get_done_state(db=db, todo_id=todo_id, user_id=user_id)


@router.delete('/todos/{todo_id}', tags=['Todo'])
def delete_todo_route(db: Session = Depends(get_db), credentials: HTTPAuthorizationCredentials = Security(security), todo_id: int = None, ):
    """API route to delete a todo instance"""
    credentials = credentials.credentials
    user_id = get_user_by_username(
        db=db, username=authentication_handler.decode_jwt_token(credentials)).id
    delete_todo(db=db, todo_id=todo_id, user_id=user_id)
    return {'message': 'Todo deleted successfully'}
