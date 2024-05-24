from pydantic import BaseModel
from typing import Optional


class SelectedCourseRead(BaseModel):
    id: int
    uid: str
    course_id: int
    group_id: Optional[int] = None


class SelectedCourseByUidRead(BaseModel):
    course_id: int
    course_name: str
    instructor_name: str


class SelectedCourseByCourseIdRead(BaseModel):
    uid: str
    name: str
    role: str
    department: str
    country: str
    email: str
    avatar: Optional[str] = None
    introduction: Optional[str] = None
    group_name: Optional[str] = None


class SelectedCourseUpdate(BaseModel):
    group_id: Optional[int] = None
    