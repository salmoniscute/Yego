from typing import Optional
from pydantic import BaseModel
from .course_bulletin import CourseBulletinRead

class CourseCreate(BaseModel):
    course_id: str
    teacher: str #wait for user
    course_code: str
    academic_year: int
    semester: int
    name: str
    outline : str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                "course_id": "CSE101",
                "teacher": "U001",
                "course_code": "CSE101",
                "academic_year": 2021,
                "semester": 1,
                "name": "Introduction to Computer Science",
                "outline": "This course is an introduction to computer science."
                }
            ]
        }
    }

class CourseRead(BaseModel):
    course_id: str
    teacher: str
    course_code: str
    academic_year: int
    semester: int
    name: str
    outline : str
    bulletins:Optional[list[CourseBulletinRead]] = None
    
class CourseUpdate(BaseModel):
    teacher : Optional[str]
    course_code : Optional[str]
    academic_year : Optional[int]
    semester : Optional[int]
    name : Optional[str]
    outline : Optional[str]
    