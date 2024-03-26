from typing import Optional
from pydantic import BaseModel
from .course_bulletin_file import CourseBulletinFileRead

class CourseBulletinCreate(BaseModel):
    cb_id: str
    publisher: str
    title: str
    release_time: str #datetime
    content: str
    pin_to_top: bool
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                "cb_id": "CB001",
                "publisher": "U001",
                "title": "Assignment 1",
                "release_time": "2021-09-01T00:00:00",
                "content": "This is the first assignment of the course.",
                "pin_to_top": "false"
                }
            ]
        }
    }
        

class CourseBulletinRead(BaseModel):
    cb_id: str
    publisher: str
    course_id: str
    title: str
    release_time: str #datetime
    content: str
    pin_to_top: bool
    files: Optional[list[CourseBulletinFileRead]] = None
    
class CourseBulletinUpdate(BaseModel):
    publisher: Optional[str]
    course_id: Optional[str]
    title: Optional[str]
    release_time: Optional[str] #Optional[datetime]
    content: Optional[str]
    pin_to_top: Optional[bool]
    