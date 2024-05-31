from pydantic import BaseModel

from schemas.component import *
from schemas.file import FileRead
from datetime import datetime
from typing import Optional


# MaterialInfo
class MaterialInfoCreate(ComponentCreate):
    start_time: datetime
    end_time: datetime
    display: bool

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Course Material 1",
                    "content": "This is the first course material of the course.",
                    "start_time": "2021-09-01T00:00:00",
                    "end_time": "2021-09-10T00:00:00",
                    "display": True
                }
            ]
        }
    }


class MaterialInfoUpdate(ComponentUpdate):
    display: Optional[bool] = None
    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "display": True,
                    "title": "Another title",
                    "content": "Another content"
                }
            ]
        }
    }


class MaterialInfoRead(BaseModel):
    id: int
    title: str
    content: str
    start_time: datetime
    end_time: datetime
    display: bool
    files: Optional[list[FileRead]] = None


# Assignment
class AssignmentCreate(ComponentCreate):
    submitted_type: str
    submitted_object: str
    display: bool
    submitted_time: datetime
    deadline: datetime
    reject_time: datetime
    feedback_type: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Course Material 1",
                    "content": "This is the first course material of the course.",
                    "submitted_type": "text",
                    "submitted_object": "team",
                    "display": False,
                    "submitted_time": "2021-09-01T00:00:00",
                    "deadline": "2021-09-10T00:00:00",
                    "reject_time": "2021-09-15T00:00:00",
                    "feedback_type": "review"
                }
            ]
        }
    }
    

class AssignmentUpdate(ComponentUpdate):
    display: Optional[bool] = None
    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "display": True,
                    "title": "Another title",
                    "content": "Another content"
                }
            ]
        }
    }


class AssignmentRead(BaseModel):
    id: int
    title: str
    content: str
    submitted_type: str
    submitted_object: str
    display: bool
    submitted_time: datetime
    deadline: datetime
    reject_time: datetime
    feedback_type: str
    files: Optional[list[FileRead]] = None


# CourseMaterial
class CourseMaterialCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Course Material 1",
                }
            ]
        }
    }


class CourseMaterialUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=100)


class CourseMaterialRead(BaseModel):
    id: int
    title: str
    material_infos: list[MaterialInfoRead]
    assignments: list[AssignmentRead]
