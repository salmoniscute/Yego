from typing import Optional
from pydantic import BaseModel

class DiscussionBase(BaseModel):
    discussion_id: str

class DiscussionCreate(DiscussionBase):
    course_id: str
    title: str
    discription: str

class DiscussionRead(DiscussionBase):
    course_id: str
    title: str
    discription: str
    
class DiscussionUpdate(BaseModel):
    # course_id: Optional[str]
    title: Optional[str]
    discription: Optional[str]
    