import email
from sqlalchemy.orm import Session

from todo.api_v1.database.models.todo_model import TodoModel
from todo.api_v1.database.models.user_model import UserModel
from todo.api_v1.database.base_actions import save_to_db, delete_from_db
from todo.api_v1.schemas.user_schema import UserCreate


def create_user(db: Session, user: UserCreate) -> UserModel:
    """
    Create a new user instance
    """
    # Create a new user instance
    user_create = UserModel(
        username=user.username, email=user.email, hashed_password=user.password + "salt")
    # Return the new user instance
    save_to_db(db=db, instance=user_create)


def get_user_by_id(db: Session, user_id: int) -> UserModel:
    """
    Get a user instance by id
    """
    # Get a user instance
    return db.query(UserModel).filter(UserModel.id == user_id).first()
