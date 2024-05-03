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
                    "release_time": "2021-09-01T00:00:00",
                    "title": "Report 1",
                    "content": "This is the first report."
                }
            ]
        }
    }

  
class ReportReplyCreate(BaseModel):
    release_time: datetime
    content: str
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "release_time": "2021-09-01T00:00:00",
                    "content": "This is the first report reply."
                }
            ]
        }
    }

    
class ReportReplyReadByID(ComponentReadID):
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


class ReportUpdate(ComponentUpdate):
    pass


class ReportReplyUpdate(ComponentUpdate):
    pass
