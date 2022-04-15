from typing import List

from sqlalchemy.orm import Session

from todo.api_v1.database.models.todo_model import TodoModel
from todo.api_v1.database.base_actions import save_to_db, delete_from_db


def create_todo(db: Session, title, description) -> TodoModel:
    """
    Create a new todo instance
    """
    # Create a new todo instance
    todo = TodoModel(title=title, description=description)
    # Return the new todo instance
    return save_to_db(db=db, instance=todo)


def get_todo(db: Session, todo_id: int) -> TodoModel:
    """
    Get a todo instance by id
    """
    # Get a todo instance
    return db.query(TodoModel).filter(TodoModel.id == todo_id).first()


def get_todo_list(db: Session) -> List[TodoModel]:
    """
    Get all todos instances
    """
    # Return all todos instances
    return db.query(TodoModel).all()


def update_todo(db: Session,
                todo_id: int,
                title: str,
                description: str,
                done: bool) -> TodoModel:
    """
    Update a todo instance
    """
    # Get todo instance to update
    todo = get_todo(db=db, todo_id=todo_id)
    # Update todo instance
    todo.title = title
    todo.description = description
    todo.done = done
    return save_to_db(db=db, instance=todo)


def get_todo_list_is_done(db: Session) -> List[TodoModel]:
    """
    Get all todos instances that are done
    """
    # Return all todos instances
    return db.query(TodoModel).filter(TodoModel.done == True).all()


def get_todo_list_not_done(db: Session) -> List[TodoModel]:
    """
    Get all todos instances that are not done
    """
    # Return all todos instances
    return db.query(TodoModel).filter(TodoModel.done == False).all()


def delete_todo(db: Session, todo_id: int) -> TodoModel:
    """
    Delete a todo instance
    """
    # Get todo instance to delete
    todo = get_todo(db=db, todo_id=todo_id)
    # Delete todo instance
    return delete_from_db(db=db, instance=todo)
