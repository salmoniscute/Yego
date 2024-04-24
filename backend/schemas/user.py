from fastapi import UploadFile
from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    uid: str
    password: str
    name: str
    role: str
    email: str
    department: str
    country: str

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
    introduction: Optional[str] = None
    avatar: Optional[str] = None


class UserUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    email: Optional[str] = None
    department: Optional[str] = None
    country: Optional[str] = None
    introduction: Optional[str] = None

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
    password: str


class UserUpdateAvatar(BaseModel):
    avatar: str
