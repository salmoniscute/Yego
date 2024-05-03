from datetime import datetime
from typing import Optional

from schemas.component import ComponentCreate, ComponentReadID, ComponentUpdate, ComponentRead
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


class ReportListRead(ComponentReadID):
    release_time: datetime
    title: str
    reply_number: int


class ReportReadByID(ComponentReadID):
    publisher: str
    publisher_avatar: Optional[str] = None
    release_time: datetime
    title: str
    content: str
    files: Optional[list[FileRead]] = None
    
      
class ReportUpdate(ComponentUpdate):
    pass

  
class ReportReplyCreate(ComponentCreate):
    parent_id: int
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "release_time": "2021-09-01T00:00:00",
                    "title": "Report Reply 1",
                    "content": "This is the first report reply.",
                    "parent_id": 1
                }
            ]
        }
    }

    
class ReportReplyRead(ComponentRead):
    parent_id: int
    root_id: int
