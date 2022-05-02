from sqlalchemy.orm import Session

# from todo.api_v1.database.models.todo_model import TodoModel
from todo.api_v1.database.models.user_model import UserModel
from todo.api_v1.database.base_actions import save_to_db
from todo.api_v1.schemas.user_schema import UserCreate
from todo.api_v1.authentication import Authentication

authentication_handler = Authentication()


def create_user(db: Session, user: UserCreate) -> None:
    """
    Create a new user instance
    """
    # Hash the password
    user.password = authentication_handler.encode_password(user.password)
    # Create a new user instance
    user_create = UserModel(
        username=user.username, email=user.email, hashed_password=user.password)
    # Return the new user instance
    save_to_db(db=db, instance=user_create)


def get_user_by_id(db: Session, user_id: int) -> UserModel:
    """
    Get a user instance by id
    """
    # Get a user instance
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_username(db: Session, username: str) -> UserModel:
    """
    Get a user instance by username
    """
    # Get a user instance
    return db.query(UserModel).filter(UserModel.username == username).first()
