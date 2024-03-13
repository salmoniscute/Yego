from typing import Optional
from pydantic import BaseModel

class DiscussionReplyBase(BaseModel):
    reply_id: str
    topic_id: str

class DiscussionReplyCreate(DiscussionReplyBase):
    publisher: str
    release_time: str
    content: str

class DiscussionReplyRead(DiscussionReplyBase):
    publisher: str
    release_time: str
    content: str
    
class DiscussionReplyUpdate(BaseModel):
    publisher: Optional[str]
    release_time: Optional[str]
    content: Optional[str]
    