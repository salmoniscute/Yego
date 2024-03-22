from typing import Optional
from pydantic import BaseModel

class DiscussionTopicFileCreate(BaseModel):
    file_id: str
    path: str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                "file_id": "F001",
                "path": "path/to/file"
                }
            ]
        }
    }

class DiscussionTopicFileRead(BaseModel):
    file_id: str
    topic_id: str
    path: str
    
class DiscussionTopicFileUpdate(BaseModel):
    path: Optional[str]
    