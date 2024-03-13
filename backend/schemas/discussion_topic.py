from typing import Optional
from pydantic import BaseModel

class DiscussionTopicBase(BaseModel):
    topic_id: str
    discussion_id: str

class DiscussionTopicCreate(DiscussionTopicBase):
    publisher: str
    title: str
    release_time: str
    content: str

class DiscussionTopicRead(DiscussionTopicBase):
    publisher: str
    title: str
    release_time: str
    content: str
    
class DiscussionTopicUpdate(BaseModel):
    publisher: Optional[str]
    title: Optional[str]
    release_time: Optional[str]
    content: Optional[str]
    