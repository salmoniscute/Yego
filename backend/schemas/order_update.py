from pydantic import BaseModel
from typing import Optional

class OrderElement(BaseModel):
    id : int
    order : int
    type : str


