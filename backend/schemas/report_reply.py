from typing import Optional
from pydantic import BaseModel

class ReportReplyBase(BaseModel):
    reply_id: str

class ReportReplyCreate(ReportReplyBase):
    parent: str
    release_time: str
    content: str

class ReportReplyRead(ReportReplyBase):
    release_time: str
    content: str
    
class ReportReplyUpdate(BaseModel):
    release_time: Optional[str]
    content: Optional[str]
    