from enum import Enum
from pydantic import BaseModel
from typing import Optional


class GroupingMethod(str, Enum):
    numbers_of_groups = "numbers_of_groups"
    numbers_of_members = "numbers_of_members"


class DistributingMethod(str, Enum):
    random = "random"
    first_name = "first_name"


class NamingRule(str, Enum):
    alphabet = "alphabet"
    number = "number"


class Member(BaseModel):
    uid: str
    name: str


class GroupCreate(BaseModel):
    name: str
    number_of_members: int


class GroupAutoCreateResponse(BaseModel):
    id: int
    name: str
    number_of_members: int
    members: Optional[list[Member]] = []


class GroupRead(BaseModel):
    id: int
    course_id: str
    name: str
    number_of_members: int


class GroupReadByCourseID(BaseModel):
    id: int
    name: str
    number_of_members: int
    members: Optional[list[Member]] = []

    
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