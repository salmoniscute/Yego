from pydantic import BaseModel
from typing import Optional


class CourseCreate(BaseModel):
    id: str
    course_code: str
    academic_year: int
    semester: int
    name: str
    outline : str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "CSE101",
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
    id: str
    uid: str
    course_code: str
    academic_year: int
    semester: int
    name: str
    outline : str
    
    
class CourseUpdate(BaseModel):
    uid : Optional[str] = None
    course_code : Optional[str] = None
    academic_year : Optional[int] = None
    semester : Optional[int] = None
    name : Optional[str] = None
    outline : Optional[str] = None
    