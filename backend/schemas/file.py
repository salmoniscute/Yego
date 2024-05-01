from pydantic import BaseModel


class FileRead(BaseModel):
    id: int
    path: str
    

