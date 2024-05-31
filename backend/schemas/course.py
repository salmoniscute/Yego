from pydantic import BaseModel, Field
from typing import Optional


class CourseCreate(BaseModel):
    course_code: str = Field(min_length=1, max_length=10)
    academic_year: int = Field(ge=2000, le=2030)
    semester: int = Field(ge=1, le=2)
    name: str = Field(min_length=1, max_length=50)
    outline : str = Field(min_length=1, max_length=1000)
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
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
    id: int
    uid: str
    course_code: str
    academic_year: int
    semester: int
    name: str
    outline : str
    
    
class CourseUpdate(BaseModel):
    uid : Optional[str] = Field(default=None, min_length=1, max_length=10)
    course_code : Optional[str] = Field(default=None, min_length=1, max_length=10)
    academic_year : Optional[int] = Field(default=None, ge=2000, le=2030)
    semester : Optional[int] = Field(default=None, ge=1, le=2)
    name : Optional[str] = Field(default=None, min_length=1, max_length=50)
    outline : Optional[str] = Field(default=None, min_length=1, max_length=1000)
    