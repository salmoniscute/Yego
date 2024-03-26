from typing import Optional
from pydantic import BaseModel
from .discussion_topic_file import DiscussionTopicFileRead
from .discussion_reply import DiscussionReplyRead

class DiscussionTopicCreate(BaseModel):
    topic_id: str
    title: str
    release_time: str
    content: str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                "topic_id": "T001",
                "title": "Topic 1",
                "release_time": "2021-09-01T00:00:00",
                "content": "This is the first topic of the discussion."
                }
            ]
        }
    }

class DiscussionTopicRead(BaseModel):
    topic_id: str
    discussion_id: str
    publisher: str
    title: str
    release_time: str
    content: str
    files:Optional[list[DiscussionTopicFileRead]] = None
    replies:Optional[list[DiscussionReplyRead]] = None
    
class DiscussionTopicUpdate(BaseModel):
    title: Optional[str]
    release_time: Optional[str]
    content: Optional[str]
    