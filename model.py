from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class ToDo(BaseModel):
    id: Optional[str] = ''  # We will generate UUIDs by ourselves!
    title: str
    description: str


class User(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        user_schema = {
            'demo_user': {
                'fullname': 'Alexander Nevsky',
                'email': 'alex@nevsky.com',
                'password': 'p@ssw0rd'
            }
        }


class Login(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        user_schema = {
            'demo_login': {
                'email': 'alex@nevsky.com',
                'password': 'p@ssw0rd'
            }
        }
