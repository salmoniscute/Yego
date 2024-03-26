from typing import Optional
from pydantic import BaseModel

class ReportReplyBase(BaseModel):
    reply_id: str
    parent: str
    report_id: str

class ReportReplyCreate(ReportReplyBase):
    publisher: str
    release_time: str
    content: str

class ReportReplyRead(ReportReplyBase):
    publisher: str
    release_time: str
    content: str
    
class ReportReplyUpdate(BaseModel):
    publisher: Optional[str]
    release_time: Optional[str]
    content: Optional[str]
    