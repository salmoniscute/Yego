from typing import Optional
from pydantic import BaseModel

from .website_bulletin_file import WebsiteBulletinFileRead


class WebsiteBulletinCreate(BaseModel):
    wb_id: str
    title: str
    release_time: str
    content: str
    pin_to_top: bool

    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "wb_id": "test",
                    "title": "Hello world",
                    "release_time": "2024-03-14 12:34:56",
                    "content": "Hello world",
                    "pin_to_top": True
                }
            ]
        }
    }


class WebsiteBulletinCreateResponse(BaseModel):
    wb_id: str
    publisher: str
    title: str
    release_time: str
    content: str
    pin_to_top: bool   


class WebsiteBulletinRead(BaseModel):
    wb_id: str
    publisher: str
    title: str
    release_time: str
    content: str
    pin_to_top: bool
    files: Optional[list[WebsiteBulletinFileRead]] = None


class WebsiteBulletinUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    pin_to_top: Optional[bool] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                { 
                    "title": "Hello world",
                    "content": "Hello world",
                    "pin_to_top": True
                }
            ]
        }
    }