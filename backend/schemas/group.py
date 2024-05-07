from enum import Enum
from pydantic import BaseModel
from typing import Optional


class GroupCreate(BaseModel):
    name: str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "A"
                }
            ]
        }
    }


class GroupRead(BaseModel):
    id: int
    course_id: str
    name: str
    
    
class GroupUpdate(BaseModel):
    name: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "B"
                }
            ]
        }
    }


class GroupingMethod(str, Enum):
    numbers_of_groups = "numbers_of_groups"
    numbers_of_members = "numbers_of_members"


class DistributingMethod(str, Enum):
    random = "random"
    first_name = "first_name"


class NamingRule(str, Enum):
    alphabet = "alphabet"
    number = "number"
    