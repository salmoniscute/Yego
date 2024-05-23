from pydantic import BaseModel
from schemas.component import *

from schemas.file import FileRead

### Discussion ###
class DiscussionCreate(ComponentCreate):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
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
    
### Discussion Topic Reply ###
class DiscussionTopicReplyCreate(BaseModel):
    content: str
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "content": "This is the first discussion topic reply of the course."
                }
            ]
        }
    }

class DiscussionTopicReplyRead(ComponentReadID):
    uid: str
    publisher: str
    avatar: Optional[str] = None
    parent_id: int
    publisher_avatar: Optional[str] = None
    release_time: datetime
    content: str

### Discussion Topic ###
class DiscussionTopicRead(ComponentReadID):
    uid: str
    publisher: str
    publisher_avatar: Optional[str] = None
    release_time: datetime
    title: str
    content: str
    files: Optional[list[FileRead]] = None
    reply_number: int
    replies: Optional[list[DiscussionTopicReplyRead]] = None

class DiscussionTopicReadlist(ComponentReadID):
    title: str
    content: str

class DiscussionOfTopics(ComponentReadWithFile):
    reply_number: int
    publisher:str
    avatar: Optional[str] = None
    subscription: bool


