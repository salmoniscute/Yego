from typing import Optional
from pydantic import BaseModel


class WebsiteBulletinFileCreate(BaseModel):
    file_id: str
    wb_id: str
    path: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "file_id": "1",
                    "wb_id": "test",
                    "path": "/path/of/file"
                }
            ]
        }
    }


class WebsiteBulletinFileCreateResponse(BaseModel):
    file_id: str


class WebsiteBulletinFileRead(BaseModel):
    file_id: str
    wb_id: str
    path: str
    

class WebsiteBulletinFileUpdate(BaseModel):
    path: str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "path": "/change/the/path/of/file"
                }
            ]
        }
    }
