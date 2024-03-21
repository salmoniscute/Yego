from typing import Optional
from pydantic import BaseModel

class DiscussionReplyCreate(BaseModel):
    reply_id: str
    publisher: str
    release_time: str
    content: str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                "reply_id": "R001",
                "publisher": "U001",
                "release_time": "2021-09-01T00:00:00",
                "content": "This is the first reply of the discussion."
                }
            ]
        }
    }

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
    