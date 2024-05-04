from pydantic import BaseModel
from schemas.component import *
### Discussion ###
class DiscussionCreate(ComponentCreate):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "release_time": "2021-09-01T00:00:00",
                    "title": "Discussion 1",
                    "content": "This is the first discussion of the course."
                }
            ]
        }
    }

class DiscussionRead(ComponentRead):
    pass
    
class DiscussionOfCourses(ComponentRead):
    subscription: bool
    
class DiscussionUpdate(ComponentUpdate):
    pass

### Discussion Topic ###
class DiscussionTopicRead(ComponentRead):
    discussion_id: int

class DiscussionOfTopics(ComponentReadWithFile):
    reply_count: int
    publisher:str
    avatar: Optional[str] = None
    subscription: bool
    
### Discussion Topic Reply ###
class DiscussionTopicReplyCreate(BaseModel):
    release_time: datetime
    content: str
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "release_time": "2021-09-01T00:00:00",
                    "content": "This is the first discussion topic reply of the course."
                }
            ]
        }
    }

class DiscussionTopicReplyRead(ComponentRead):
    parent_id: int
    root_id: int




