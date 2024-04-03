from typing import Optional
from pydantic import BaseModel


class FileCreate(BaseModel):
    id: str
    path: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "id": "1",
                    "path": "/path/of/file"
                }
            ]
        }
    }


class FileRead(BaseModel):
    id: str
    owner: str
    component_id: str
    path: str
    

class FileUpdate(BaseModel):
    path:  Optional[str]
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "path": "/change/the/path/of/file"
                }
            ]
        }
    }
