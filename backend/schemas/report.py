from typing import Optional
from pydantic import BaseModel

class ReportBase(BaseModel):
    report_id: str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "report_id": "1",
                    "title": "website login error",
                    "release_time": "2024-03-20",
                    "content": "I can not login the website though posting this report needs to login haha.",
                }
            ]
        }
    }

class ReportCreate(ReportBase):
    title: str
    release_time: str
    content: str

class ReportRead(ReportBase):
    title: str
    release_time: str
    reply_number: int
    
class ReportUpdate(BaseModel):
    title: Optional[str]
    release_time: Optional[str]
    content: Optional[str]
    