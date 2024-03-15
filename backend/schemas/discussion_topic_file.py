from typing import Optional
from pydantic import BaseModel

class DiscussionTopicFileBase(BaseModel):
    file_id: str
    topic_id: str

class DiscussionTopicFileCreate(DiscussionTopicFileBase):
    path: str

class DiscussionTopicFileRead(DiscussionTopicFileBase):
    path: str
    
class DiscussionTopicFileUpdate(BaseModel):
    path: Optional[str]
    