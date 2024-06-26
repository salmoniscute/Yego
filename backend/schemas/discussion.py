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


class DiscussionRead(ComponentReadID):
    uid: str
    title: str
    content: str
    

class DiscussionOfCourses(ComponentReadID):
    uid: str
    title: str
    content: str
    subscription_status: bool

    
class DiscussionUpdate(ComponentUpdate):
    pass
    

### Discussion Topic Reply ###
class DiscussionTopicReplyCreate(BaseModel):
    content: str = Field(min_length=1, max_length=1000)
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
    subscription_status: bool
