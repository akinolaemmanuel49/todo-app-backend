import datetime
import re

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import validates, relationship

from todo.api_v1.database.config import Base
from todo.api_v1.database.models.todo_model import TodoModel


class UserModel(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(10), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    profile_image = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    created_at = Column(
        DateTime, default=lambda: datetime.datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.datetime.utcnow(
    ), onupdate=lambda: datetime.datetime.utcnow(), nullable=False)

    todos = relationship("TodoModel", back_populates="owner",
                         cascade="all, delete-orphan")

    @validates("username")
    def validate_username(self, key, username):
        if len(username) > 10:
            raise ValueError("Username must be less than 10 characters")
        elif len(username) < 3:
            raise ValueError("Username must be atleast than 2 characters")
        else:
            return username

    @validates("email")
    def validate_email(self, key, email):
        if len(email) > 255:
            raise ValueError("Email must be less than 255 characters")
        elif len(email) < 3:
            raise ValueError("Email must be atleast than 2 characters")
        elif not re.match(
                r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            raise ValueError("Email must be valid")
        else:
            return email

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def __repr__(self):
        return "< UserModel(username={}, email={}, created_at={},\
                            updated_at={}) >".format(self.username,
                                                     self.email,
                                                     self.created_at,
                                                     self.updated_at)
