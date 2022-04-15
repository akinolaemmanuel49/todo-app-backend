from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from todo.api_v1.config import Config
from todo.api_v1.schemas.todo_schema import Todo, TodoCreate, TodoUpdate
from todo.api_v1.dependencies.database import get_db
from todo.api_v1.database.actions.todo_actions import (create_todo,
                                                       get_todo_list,
                                                       update_todo,
                                                       delete_todo,
                                                       get_todo,
                                                       get_todo_list_is_done,
                                                       get_todo_list_not_done)

router = APIRouter(prefix=Config.API_VERSION_STRING, tags=['Todo'])


@router.post('/todos', response_model=Todo)
def create_todo_route(todo: TodoCreate,
                      db: Session = Depends(get_db)) -> dict:
    return create_todo(db=db, title=todo.title, description=todo.description)


@router.get('/todos/complete', response_model=List[Todo])
def get_todos_is_done_route(db: Session = Depends(get_db)):
    return get_todo_list_is_done(db=db)


@router.get('/todos/incomplete', response_model=List[Todo])
def get_todos_is_not_done_route(db: Session = Depends(get_db)):
    return get_todo_list_not_done(db=db)


@router.get('/todos', response_model=List[Todo])
def get_todos_route(db: Session = Depends(get_db)):
    return get_todo_list(db=db)


@router.get('/todos/{todo_id}', response_model=Todo)
def get_todo_route(db: Session = Depends(get_db), todo_id: int = None):
    return get_todo(db=db, todo_id=todo_id)


@router.put('/todos/{todo_id}', response_model=Todo)
def update_todo_route(todo_id: int,
                      todo: TodoUpdate,
                      db: Session = Depends(get_db)):
    return update_todo(db=db,
                       todo_id=todo_id,
                       title=todo.title,
                       description=todo.description,
                       done=todo.done)


@router.delete('/todos/{todo_id}', response_model=Todo)
def delete_todo_route(db: Session = Depends(get_db), todo_id: int = None, ):
    return delete_todo(db=db, todo_id=todo_id)
