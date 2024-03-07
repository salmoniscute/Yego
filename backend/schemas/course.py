from typing import Optional
from pydantic import BaseModel

class CourseBase(BaseModel):
    course_id: str

class CourseCreate(CourseBase):
    teacher: str
    course_code: str
    academic_year: int
    semester: int
    name: str
    outline : str

class CourseRead(CourseBase):
    course_id: str
    teacher: str
    course_code: str
    academic_year: int
    semester: int
    name: str
    outline : str
    
class CourseUpdate(BaseModel):
    teacher : Optional[str]
    course_code : Optional[str]
    academic_year : Optional[int]
    semester : Optional[int]
    name : Optional[str]
    outline : Optional[str]
    