from typing import Optional

from schemas.component import ComponentRead


class BulletinCreate(ComponentRead):
    course_id: str
    type: str
    pin_to_top: bool
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "1",
                    "publisher": "C14096277",
                    "release_time": "2021-09-01T00:00:00",
                    "title": "Assignment 1",
                    "content": "This is the first assignment of the course.",
                    "course_id": "CSE101",
                    "type": "CourseBulletin",
                    "pin_to_top": "false"
                }
            ]
        }
    }
        

class BulletinRead(ComponentRead):
    course_id: str
    type: str
    pin_to_top: bool
    

class BulletinUpdate(ComponentRead):
    course_id: Optional[str] = None
    type: Optional[str] = None
    pin_to_top: Optional[bool] = None
    