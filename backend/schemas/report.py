from schemas.component import ComponentCreate, ComponentRead, ComponentUpdate
from pydantic import BaseModel

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


class ReportRead(BaseModel):
    id: int
    release_time: str
    title: str
    reply_count: int

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

