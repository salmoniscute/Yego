from pydantic import BaseModel, Field
from typing import Optional


class SelectedCourseRead(BaseModel):
    id: int
    uid: str
    course_id: int
    group_id: Optional[int] = None


class SelectedCourseByUidRead(BaseModel):
    course_id: int
    instructor_name: str
    course_code: str
    academic_year: int
    semester: int
    course_name: str
    outline : str


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
