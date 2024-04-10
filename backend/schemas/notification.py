from pydantic import BaseModel


class NotificationCreate(BaseModel):
    have_read: bool
    release_time: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "have_read": False,
                    "release_time": "2021-09-01 00:00:00"
                }
            ]
        }
    }


class NotificationRead(BaseModel):
    uid: str
    component_id: str
    have_read: bool
    release_time: str
    

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
