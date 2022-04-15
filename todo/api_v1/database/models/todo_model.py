import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean

from database.config import Base


class TodoModel(Base):
    """
    Todo Model
    """
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(128), nullable=False)
    description = Column(String(256), nullable=True)
    done = Column(Boolean, default=False)
    created_at = Column(
        DateTime, default=lambda: datetime.datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.datetime.utcnow(
    ), on_update=lambda: datetime.datetime.utcnow(), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "done": self.done,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def __repr__(self):
        return "< TodoModel(title={}, description={}, done={}, created_at={},\
                            updated_at={}) >".format(self.title,
                                                     self.description,
                                                     self.done,
                                                     self.created_at,
                                                     self.updated_at)
