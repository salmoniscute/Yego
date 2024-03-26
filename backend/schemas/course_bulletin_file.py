from typing import Optional
from pydantic import BaseModel

class CourseBulletinFileCreate(BaseModel):
    file_id: str
    path: str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                "file_id": "F001",
                "path": "https://www.google.com"
                }
            ]
        }
    }
        

class CourseBulletinFileRead(BaseModel):
    file_id: str
    path: str
    cb_id: str
    
class CourseBulletinFileUpdate(BaseModel):
    path: Optional[str]

    