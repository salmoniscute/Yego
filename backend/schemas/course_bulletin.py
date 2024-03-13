from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class CourseBulletinBase(BaseModel):
    cb_id: str

class CourseBulletinCreate(CourseBulletinBase):
    publisher: str
    course_id: str
    title: str
    release_time: str #datetime
    content: str

class CourseBulletinRead(CourseBulletinBase):
    publisher: str
    course_id: str
    title: str
    release_time: str #datetime
    content: str
    
class CourseBulletinUpdate(BaseModel):
    publisher: Optional[str]
    course_id: Optional[str]
    title: Optional[str]
    release_time: Optional[str] #Optional[datetime]
    content: Optional[str]
    