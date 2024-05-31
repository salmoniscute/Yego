from pydantic import BaseModel, Field
from typing import Optional


class UserCreate(BaseModel):
    uid: str = Field(min_length=1, max_length=10)
    password: str = Field(min_length=6, max_length=20)
    name: str = Field(min_length=1, max_length=50)
    role: str = Field(min_length=1, max_length=10)
    email: str = Field(min_length=1, max_length=100)
    department: str = Field(min_length=1, max_length=50)
    country: str = Field(min_length=1, max_length=20)

    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "uid": "C14096277",
                    "password": "test123",
                    "name": "nt1026",
                    "role": "student",
                    "email": "C14096277@gs.ncku.edu.tw",
                    "department": "Mathematics",
                    "country": "Taiwan"
                }
            ]
        }
    }


class UserRead(BaseModel):
    uid: str
    name: str
    role: str
    email: str
    department: str
    country: str
    introduction: Optional[str]
    avatar: Optional[str]


class UserUpdate(BaseModel):
    name: str = Field(default=None, min_length=1, max_length=50)
    role: str = Field(default=None, min_length=1, max_length=10)
    email: str = Field(default=None, min_length=1, max_length=100)
    department: str = Field(default=None, min_length=1, max_length=50)
    country: str = Field(default=None, min_length=1, max_length=20)
    introduction: Optional[str] = Field(default=None, min_length=1, max_length=1000)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "nt1026",
                    "role": "student",
                    "email": "C14096277@gs.ncku.edu.tw",
                    "department": "Mathematics",
                    "country": "Taiwan",
                    "introduction": "hello world"
                }
            ]
        }
    }


class UserUpdatePassword(BaseModel):
    password: str = Field(min_length=6, max_length=20)
