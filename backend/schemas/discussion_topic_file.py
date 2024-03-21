from typing import Optional
from pydantic import BaseModel

class DiscussionTopicFileCreate(BaseModel):
    file_id: str
    path: str

class DiscussionTopicFileRead(BaseModel):
    file_id: str
    topic_id: str
    path: str
    
class DiscussionTopicFileUpdate(BaseModel):
    path: Optional[str]
    