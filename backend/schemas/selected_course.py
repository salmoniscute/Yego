from typing import Optional
from pydantic import BaseModel


class SelectedCourseCreate(BaseModel):
    uid: str
    course_id: str
    group: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "uid": "C14096277",
                    "course_id": "test",
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
    

class SelectedCourseUpdate(BaseModel):
    group: str
    