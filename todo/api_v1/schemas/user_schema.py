import re

from pydantic import BaseModel, EmailStr, validator


class UserBase(BaseModel):
    username: str
    email: EmailStr

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

    @validator("password")
    def check_password(cls, v, values):
        if 'password' in values and 'confirm_password' in values:
            if values['password'] != values['confirm_password']:
                raise ValueError("Passwords don't match")
        return v

    @validator("email")
    def check_email(cls, v):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if (re.fullmatch(regex, v) is None):
            raise ValueError("Invalid email.")
        return v


class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "JohnDoe",
                "email": "johndoe@mail.com",
                "created_at": "2020-01-01T00:00:00",
                "updated_at": "2020-01-01T00:00:00"
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


class TokenData(BaseModel):
    access_token: str
    refresh_token: str


class AccessTokenData(BaseModel):
    access_token: str
