from pydantic import BaseModel, validator


class TodoBase(BaseModel):
    todo: str

    @validator('todo')
    def validate_todo(cls, v):
        if len(v) > 64:
            raise ValueError(
                'Todo must be less than 64 characters')
        elif len(v) < 1:
            raise ValueError('Todo must be at least 1 character')
        else:
            return v


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    done: bool


class Todo(BaseModel):
    id: int
    todo: str
    done: bool = False

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "todo": "Buy milk",
                "done": False
            }
        }
