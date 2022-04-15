from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    description: str = None

    class Config:
        schema_extra = {
            "example": {
                "title": "Buy milk",
                "description": "Milk for baby",
            }
        }


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    done: bool

    class Config:
        schema_extra = {
            "example": {
                "title": "Buy milk",
                "description": "Milk for baby",
                "done": False,
            }
        }


class Todo(BaseModel):
    id: int
    title: str
    description: str = None
    done: bool = False

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "title": "Buy milk",
                "description": "Milk for baby",
                "done": False
            }
        }
