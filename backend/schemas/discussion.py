from typing import Optional
from pydantic import BaseModel
from .discussion_topic import DiscussionTopicRead

class DiscussionCreate(BaseModel):
    discussion_id: str
    title: str
    discription: str
    
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                "discussion_id": "D001",
                "title": "Discussion 1",
                "discription": "This is the first discussion of the course."
                }
            ]
        }
    }

class DiscussionRead(BaseModel):
    discussion_id: str
    course_id: str
    title: str
    discription: str
    topics:Optional[list[DiscussionTopicRead]] = None
    
class DiscussionUpdate(BaseModel):
    title: Optional[str]
    discription: Optional[str]
    