from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from schemas import file as FileSchema


class ComponentCreate(BaseModel):
    release_time: datetime
    title: str
    content: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "release_time": "2024-04-02 16:00:00",
                    "title": "This is a title",
                    "content": "This is a content"
                }
            ]
        }
    }

class ComponentReadID(BaseModel):
    id: int
    

class ComponentRead(BaseModel):
    id: int
    uid: str
    title: str
    content: str


class ComponentReadWithFile(BaseModel):
    id: int
    uid: str
    release_time: datetime
    title: str
    content: str
    files: Optional[list[FileSchema.FileRead]] = None
       

class ComponentUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    
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
