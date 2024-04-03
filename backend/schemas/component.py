from typing import Optional
from pydantic import BaseModel


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
    publisher: str
    release_time: str
    title: str
    content: str
    

class ComponentUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]
    
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
