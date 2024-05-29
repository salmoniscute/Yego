from datetime import datetime
from pydantic import BaseModel
from typing import Optional

from schemas.component import ComponentCreate, ComponentReadID, ComponentUpdate
from schemas.file import FileRead


class ReportCreate(ComponentCreate):    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Report 1",
                    "content": "This is the first report."
                }
            ]
        }
    }

  
class ReportReplyCreate(BaseModel):
    content: str
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "content": "This is the first report reply."
                }
            ]
        }
    }

    
class ReportReplyReadByID(ComponentReadID):
    uid: str
    publisher: str
    avatar: Optional[str] = None
    parent_id: int
    publisher: str
    publisher_avatar: Optional[str] = None
    release_time: datetime
    content: str


class ReportReadByID(ComponentReadID):
    publisher: str
    publisher_avatar: Optional[str] = None
    release_time: datetime
    title: str
    content: str
    files: Optional[list[FileRead]] = None
    replies: Optional[list[ReportReplyReadByID]] = None


class ReportListRead(ComponentReadID):
    release_time: datetime
    title: str
    reply_number: int
    subscription_status: bool


class ReportUpdate(ComponentUpdate):
    pass


class ReportReplyUpdate(ComponentUpdate):
    pass
