from pydantic import BaseModel


class FileCreate(BaseModel):
    path: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "path": "/path/of/file"
                }
            ]
        }
    }


class FileRead(BaseModel):
    id: int
    component_id: int
    path: str
    

class FileUpdate(BaseModel):
    path:  str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "path": "/change/the/path/of/file"
                }
            ]
        }
    }
