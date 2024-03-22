from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class CourseBulletinCreate(BaseModel):
    cb_id: str
    publisher: str
    # course_id: str
    title: str
    release_time: str #datetime
    content: str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                "cb_id": "CB001",
                "publisher": "U001",
                "title": "Assignment 1",
                "release_time": "2021-09-01T00:00:00",
                "content": "This is the first assignment of the course."
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
    
class CourseBulletinUpdate(BaseModel):
    publisher: Optional[str]
    course_id: Optional[str]
    title: Optional[str]
    release_time: Optional[str] #Optional[datetime]
    content: Optional[str]
    