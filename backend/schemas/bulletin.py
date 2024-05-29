from datetime import datetime
from typing import Optional

from schemas.component import ComponentCreate, ComponentReadID, ComponentUpdate
from schemas.file import FileRead


class BulletinCreate(ComponentCreate):
    pin_to_top: bool
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Bulletin 1",
                    "content": "This is the first bulletin of the course.",
                    "pin_to_top": "false"
                }
            ]
        }
    }


class CourseBulletinListRead(ComponentReadID):
    uid: str
    publisher: str
    publisher_avatar: Optional[str] = None
    release_time: datetime
    title: str
    content: str
    pin_to_top: bool
    subscription_status: bool
    files: Optional[list[FileRead]] = None


class WebsiteBulletinListRead(ComponentReadID):
    publisher: str
    release_time: datetime
    title: str
    pin_to_top: bool
    

class BulletinReadByID(ComponentReadID):
    publisher: str
    publisher_avatar: Optional[str] = None
    release_time: datetime
    title: str
    content: str
    pin_to_top: bool
    files: Optional[list[FileRead]] = None


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
    