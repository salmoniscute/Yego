from pydantic import BaseModel
from datetime import datetime

class NotificationCreate(BaseModel):
    have_read: bool
    release_time: datetime
    type: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "have_read": False,
                    "release_time": "2021-09-01 00:00:00",
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
    

class NotificationUpdate(BaseModel):
    have_read: bool
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "have_read": True
                }
            ]
        }
    }
