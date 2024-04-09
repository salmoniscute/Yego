from typing import Optional

from schemas.component import ComponentCreate, ComponentRead, ComponentReadWithFile, ComponentUpdate


class BulletinCreate(ComponentCreate):
    pin_to_top: bool
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "1",
                    "release_time": "2021-09-01T00:00:00",
                    "title": "Bulletin 1",
                    "content": "This is the first bulletin of the course.",
                    "pin_to_top": "false"
                }
            ]
        }
    }

class CourseBulletinCreateResponse(ComponentRead):
    course_id: str
    type: str
    pin_to_top: bool


class WebsiteBulletinCreateResponse(ComponentRead):
    type: str
    pin_to_top: bool


class CourseBulletinRead(ComponentReadWithFile):
    course_id: str
    type: str
    pin_to_top: bool


class WebsiteBulletinRead(ComponentReadWithFile):
    type: str
    pin_to_top: bool
    

class BulletinUpdate(ComponentUpdate):
    pin_to_top: Optional[bool] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "title": "Another title",
                    "content": "Another content",
                    "pin_to_top": True
                }
            ]
        }
    }
    