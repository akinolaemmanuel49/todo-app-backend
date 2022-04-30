from pydantic import BaseModel, validator, ValidationError


class TodoBase(BaseModel):
    todo: str

    @validator('todo')
    def validate_todo(cls, v):
        if len(v) > 128:
            raise ValueError(
                'Todo must be less than 128 characters')
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
