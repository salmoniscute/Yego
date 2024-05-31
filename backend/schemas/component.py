from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from schemas import file as FileSchema


class ComponentCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1, max_length=1000)

    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "title": "This is a title",
                    "content": "This is a content"
                }
            ]
        }
    }

class ComponentReadID(BaseModel):
    id: int


class ComponentReadWithFile(BaseModel):
    id: int
    uid: str
    release_time: datetime
    title: str
    content: str
    files: Optional[list[FileSchema.FileRead]] = None
       

class ComponentUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=100)
    content: Optional[str] = Field(default=None, min_length=1, max_length=1000)
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "title": "Another title",
                    "content": "Another content"
                }
            ]
        }
    }
