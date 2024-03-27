from typing import Optional
from pydantic import BaseModel

class ReportFileBase(BaseModel):
    file_id: str

class ReportFileCreate(ReportFileBase):
    path: str

class ReportFileRead(ReportFileBase):
    path: str
    
class ReportFileUpdate(BaseModel):
    path: Optional[str]
    