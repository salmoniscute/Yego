from typing import Optional
from pydantic import BaseModel


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


class SelectedCourseCreateResponse(BaseModel):
    uid: str
    course_id: str
    group: Optional[str] = None


class SelectedCourseRead(BaseModel):
    uid: str
    course_id: str
    group: str


class SelectedCourseByUidRead(BaseModel):
    course_name: str
    teacher_name: str


class SelectedCourseByCourseIdRead(BaseModel):
    name: str
    uid: str
    department: str
    role: str
    group: Optional[str] = None


class SelectedCourseUpdate(BaseModel):
    group: str
    