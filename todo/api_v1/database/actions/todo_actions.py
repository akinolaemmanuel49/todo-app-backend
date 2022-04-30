from typing import List

from sqlalchemy.orm import Session

from todo.api_v1.database.models.todo_model import TodoModel
from todo.api_v1.database.base_actions import save_to_db, delete_from_db


def create_todo(db: Session, todo) -> TodoModel:
    """
    Create a new todo instance
    """
    # Create a new todo instance
    todo_create = TodoModel(todo=todo)
    # Return the new todo instance
    save_to_db(db=db, instance=todo_create)


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
    return db.query(TodoModel).order_by(TodoModel.id.desc()).all()


def toggle_done(db: Session, todo_id: int) -> TodoModel:
    """
    Toggle a todo instance done
    """
    # Get todo instance to toggle
    todo_toggle = get_todo(db=db, todo_id=todo_id)
    # Toggle todo instance
    todo_toggle.done = not todo_toggle.done
    save_to_db(db=db, instance=todo_toggle)


def get_done_state(db: Session, todo_id: int) -> TodoModel:
    """
    Get whether a todo instance is done or not.
    """
    todo_done = get_todo(db=db, todo_id=todo_id)
    return todo_done.done


def update_todo(db: Session,
                todo_id: int,
                todo: str,
                done: bool) -> TodoModel:
    """
    Update a todo instance
    """
    # Get todo instance to update
    todo_update = get_todo(db=db, todo_id=todo_id)
    # Update todo instance
    todo_update.todo = todo
    todo_update.done = done
    save_to_db(db=db, instance=todo_update)


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
    todo_delete = get_todo(db=db, todo_id=todo_id)
    # Delete todo instance
    delete_from_db(db=db, instance=todo_delete)
