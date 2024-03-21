from typing import Optional
from pydantic import BaseModel

class DiscussionReplyCreate(BaseModel):
    reply_id: str
    publisher: str
    release_time: str
    content: str

class DiscussionReplyRead(BaseModel):
    reply_id: str
    topic_id: str
    publisher: str
    release_time: str
    content: str
    
class DiscussionReplyUpdate(BaseModel):
    publisher: Optional[str]
    release_time: Optional[str]
    content: Optional[str]
    