from schemas.component import *
from datetime import datetime
from typing import Optional

class CourseMaterialCreate(ComponentCreate):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "release_time": "2021-09-01T00:00:00",
                    "title": "Course Material 1",
                    "content": "This is the first course material of the course."
                }
            ]
        }
    }
    

class CourseMaterialRead(ComponentRead):
    pass


class CourseMaterialUpdate(ComponentUpdate):
    pass

class MaterialInfoCreate(ComponentCreate):
    type: str
    start_time: datetime
    end_time: datetime
    assignment_reject_time: datetime
    display: bool
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "release_time": "2021-09-01T00:00:00",
                    "title": "Course Material 1",
                    "content": "This is the first course material of the course.",
                    "type": "Assignment",
                    "start_time": "2021-09-01T00:00:00",
                    "end_time": "2021-09-10T00:00:00",
                    "assignment_reject_time": "2021-09-15T00:00:00",
                    "display": True
                }
            ]
        }
    }

class MaterialInfoUpdate(ComponentUpdate):
    type: Optional[str]
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    assignment_reject_time: Optional[datetime]
    display: Optional[bool]
    
class MaterialInfoRead(ComponentRead):
    type: str
    start_time: datetime
    end_time: datetime
    assignment_reject_time: datetime
    display: bool
    
class SubmittedMaterialCreate(ComponentCreate):
    pass

class SubmittedMaterialUpdate(ComponentUpdate):
    grade: Optional[int]
    
class SubmittedMaterialRead(ComponentRead):
    grade: int
    assignment_id: int