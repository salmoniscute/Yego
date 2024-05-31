from enum import Enum
from pydantic import BaseModel, Field
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
    uid: str = Field(min_length=1, max_length=10)
    name: str = Field(min_length=1, max_length=50)


class GroupCreate(BaseModel):
    name: str
    number_of_members: int


class GroupManualCreate(BaseModel):
    name: str = Field(min_length=1, max_length=20)
    members: Optional[list[Member]] = []

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "A",
                    "members": [
                        {
                            "uid": "C14096277",
                            "name": "nt1026"
                        },
                        {
                            "uid": "F74102048",
                            "name": "little ming"
                        }
                    ]
                }
            ]
        }
    
    }


class GroupAutoCreateResponse(BaseModel):
    name: str = Field(min_length=1, max_length=20)
    number_of_members: int = Field(ge=1)
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
    name: Optional[str] = Field(default=None, min_length=1, max_length=20)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "B"
                }
            ]
        }
    }