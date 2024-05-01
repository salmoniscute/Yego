from datetime import datetime
from pydantic import BaseModel
from typing import Optional

from schemas.component import ComponentCreate, ComponentRead, ComponentReadWithFile, ComponentUpdate
from schemas import file as FileSchema


class BulletinCreate(ComponentCreate):
    pin_to_top: bool
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "release_time": "2021-09-01T00:00:00",
                    "title": "Bulletin 1",
                    "content": "This is the first bulletin of the course.",
                    "pin_to_top": "false"
                }
            ]
        }
    }


class BulletinListRead(BaseModel):
    id: int
    publisher: str
    release_time: datetime
    title: str
    pin_to_top: bool


class BulletinRead(BaseModel):
    id: int
    uid: str
    release_time: datetime
    title: str
    content: str
    pin_to_top: bool
    type: str
    pin_to_top: bool


class BulletinReadByID(BaseModel):
    id: int
    publisher: str
    publisher_avatar: Optional[str] = None
    release_time: datetime
    title: str
    content: str
    pin_to_top: bool
    files: Optional[list[FileSchema.FileRead]] = None


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
    

class CourseBulletinRead(BulletinRead):
    course_id: str


class WebsiteBulletinRead(BulletinRead):
    pass
