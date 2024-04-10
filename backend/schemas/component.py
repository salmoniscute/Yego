from pydantic import BaseModel
from typing import Optional

from schemas import file as FileSchema


class ComponentCreate(BaseModel):
    id: str
    release_time: str
    title: str
    content: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "id": "1",
                    "release_time": "2024-04-02 16:00:00",
                    "title": "This is a title",
                    "content": "This is a content"
                }
            ]
        }
    }


class ComponentRead(BaseModel):
    id: str
    uid: str
    release_time: str
    title: str
    content: str


class ComponentReadWithFile(BaseModel):
    id: str
    uid: str
    release_time: str
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
