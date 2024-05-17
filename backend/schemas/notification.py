from pydantic import BaseModel
from datetime import datetime


class NotificationCreate(BaseModel):
    have_read: bool
    type: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "have_read": False,
                    "type": "website_bulletin"
                }
            ]
        }
    }


class NotificationRead(BaseModel):
    id: int
    uid: str
    component_id: int
    have_read: bool
    release_time: datetime
    type: str


class NotificationReadByUid(BaseModel):
    id: int
    uid: str
    component_id: int
    publisher: str
    course_name: str
    release_time: datetime
    title: str
    content: str
    have_read: bool
    icon_type: str
