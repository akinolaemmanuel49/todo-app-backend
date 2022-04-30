import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import validates, relationship

from todo.api_v1.database.config import Base
# from todo.api_v1.database.models.user_model import UserModel


class TodoModel(Base):
    """
    Todo Model
    """
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    todo = Column(String(64), nullable=False)
    done = Column(Boolean, default=False, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(
        DateTime, default=lambda: datetime.datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.datetime.utcnow(
    ), onupdate=lambda: datetime.datetime.utcnow(), nullable=False)

    owner = relationship("UserModel", back_populates="todos")

    @validates("todo")
    def validate_todo(self, key, todo):
        if len(todo) > 64:
            raise ValueError("Todo must be less than 64 characters")
        elif len(todo) < 1:
            raise ValueError("Todo must be at least 1 character")
        else:
            return todo

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.todo,
            "done": self.done,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def __repr__(self):
        return "< TodoModel(title={}, description={}, done={}, created_at={},\
                            updated_at={}) >".format(self.todo,
                                                     self.done,
                                                     self.created_at,
                                                     self.updated_at)
