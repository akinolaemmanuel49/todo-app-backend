import datetime
import re
from pydantic import BaseModel, validator, root_validator


class UserBase(BaseModel):
    username: str
    email: str

    @validator("username")
    def validate_username(cls, v):
        if len(v) > 10:
            raise ValueError("Username must be less than 10 characters")
        elif len(v) < 3:
            raise ValueError("Username must be atleast than 2 characters")
        else:
            return v


class UserCreate(UserBase):
    password: str
    confirm_password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "JohnDoe",
                "email": "johndoe@mail.com",
                "password": "password",
                "confirm_password": "password"
            }
        }

    @validator("password")
    def validate_password(cls, v):
        if len(v) > 64:
            raise ValueError("Password must be less than 64 characters")
        elif len(v) < 6:
            raise ValueError("Password must be atleast than 6 characters")
        else:
            return v

    @root_validator()
    def check_password_match(cls, values):
        password = values["password"]
        confirm_password = values["confirm_password"]

        if password != confirm_password:
            raise ValueError("Passwords do not match")
        return values

    @validator("email")
    def check_email(cls, v):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if (re.fullmatch(regex, v) is None):
            raise ValueError("Invalid email address.")
        return v


class User(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "JohnDoe",
                "email": "johndoe@mail.com",
                "created_at": datetime.datetime.utcnow(),
                "updated_at": datetime.datetime.utcnow()
            }
        }


class Credentials(BaseModel):
    username: str
    password: str

    @validator("username")
    def check_username(cls, v):
        if len(v) < 3:
            raise ValueError("Username must be atleast than 2 characters")
        elif len(v) > 10:
            raise ValueError("Username must be less than 10 characters")
        else:
            return v

    @validator("password")
    def check_password(cls, v):
        if len(v) < 6:
            raise ValueError("Password must be atleast than 6 characters")
        elif len(v) > 64:
            raise ValueError("Password must be less than 64 characters")
        else:
            return v

    class Config:
        schema_extra = {
            "example": {
                "username": "JohnDoe",
                "password": "password"
            }
        }


class TokenData(BaseModel):
    access_token: str
    refresh_token: str


class AccessTokenData(BaseModel):
    access_token: str


class UserProfile(BaseModel):
    username: str
    profile_image: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "JohnDoe",
                "profile_image": "https://www.example.com/image.jpg"
            }
        }
