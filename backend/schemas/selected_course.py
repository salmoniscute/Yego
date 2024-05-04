from pydantic import BaseModel
from typing import Optional


class SelectedCourseCreate(BaseModel):
    group: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "group": "A"
                }
            ]
        }
    }


class SelectedCourseRead(BaseModel):
    id: int
    uid: str
    course_id: str
    group: Optional[str] = None


class SelectedCourseByUidRead(BaseModel):
    course_id: str
    course_name: str
    instructor_name: str


class SelectedCourseByCourseIdRead(BaseModel):
    uid: str
    name: str
    role: str
    department: str
    country: str
    email: str
    avatar: Optional[str] = None
    introduction: Optional[str] = None
    group: Optional[str] = None


class SelectedCourseUpdate(BaseModel):
    group: Optional[str] = None
    