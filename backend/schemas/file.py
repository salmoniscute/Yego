from pydantic import BaseModel


class FileRead(BaseModel):
    id: int
    component_id: int
    path: str
    

