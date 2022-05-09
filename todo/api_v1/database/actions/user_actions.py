from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from todo.api_v1.schemas.error_response_schema import ErrorResponse
from todo.api_v1.database.models.user_model import UserModel
from todo.api_v1.database.base_actions import save_to_db
from todo.api_v1.schemas.user_schema import UserCreate
from todo.api_v1.authentication import Authentication

authentication_handler = Authentication()


def create_user(db: Session, user: UserCreate) -> None:
    """
    Create a new user instance
    """
    try:
        # Hash the password
        user.password = authentication_handler.encode_password(user.password)
        if get_user_by_username(db=db, username=user.username):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=jsonable_encoder(
                ErrorResponse(code=status.HTTP_409_CONFLICT, message='Username already exists')))
        if get_user_by_email(db=db, email=user.email):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=jsonable_encoder(
                ErrorResponse(code=status.HTTP_409_CONFLICT, message='Email already exists')))
        # Create a new user instance
        user_create = UserModel(
            username=user.username, email=user.email, hashed_password=user.password)
        # Return the new user instance
        save_to_db(db=db, instance=user_create)
    except Exception as e:
        db.rollback()
        raise e


def get_user_by_id(db: Session, user_id: int) -> UserModel:
    """
    Get a user instance by id
    """
    # Get a user instance
    try:
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=jsonable_encoder(
                ErrorResponse(code=status.HTTP_404_NOT_FOUND, message='User not found')))
        return user
    except Exception as e:
        db.rollback()
        raise e


def get_user_by_username(db: Session, username: str) -> UserModel:
    """
    Get a user instance by username
    """
    try:
        # Get a user instance
        user = db.query(UserModel).filter(
            UserModel.username == username).first()
        return user
    except Exception as e:
        db.rollback()
        if isinstance(e, SQLAlchemyError):
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=jsonable_encoder(
                ErrorResponse(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message='Internal server error')))
        else:
            raise e


def get_user_by_email(db: Session, email: str) -> UserModel:
    """
    Get a user instance by email
    """
    try:
        # Get a user instance
        user = db.query(UserModel).filter(
            UserModel.email == email).first()
        return user
    except Exception as e:
        db.rollback()
        if isinstance(e, SQLAlchemyError):
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=jsonable_encoder(
                ErrorResponse(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message='Internal server error')))
        else:
            raise e
