from typing import Optional

from schemas.component import ComponentCreate, ComponentRead, ComponentUpdate


class CourseBulletinCreate(ComponentCreate):
    pin_to_top: bool
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "1",
                    "release_time": "2021-09-01T00:00:00",
                    "title": "Assignment 1",
                    "content": "This is the first assignment of the course.",
                    "pin_to_top": "false"
                }
            ]
        }
    }


class CourseBulletinRead(ComponentRead):
    course_id: str
    type: str
    pin_to_top: bool
    

class CourseBulletinUpdate(ComponentUpdate):
    course_id: Optional[str] = None
    pin_to_top: Optional[bool] = None
    