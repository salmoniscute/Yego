from typing import Optional
from pydantic import BaseModel

class DiscussionCreate(BaseModel):
    discussion_id: str
    title: str
    discription: str

class DiscussionRead(BaseModel):
    discussion_id: str
    course_id: str
    title: str
    discription: str
    
class DiscussionUpdate(BaseModel):
    title: Optional[str]
    discription: Optional[str]
    