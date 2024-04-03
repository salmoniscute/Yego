from sqlalchemy import String, DateTime, Boolean, String
from sqlalchemy.orm import DeclarativeBase, mapped_column
from typing import Annotated, Optional
from datetime import datetime

class Base(DeclarativeBase):
    pass


class BaseType:
    id = Annotated[int, mapped_column(String(10), primary_key=True)]
    hashed_password = Annotated[str, mapped_column(String(60))]
    boolean = Annotated[bool, mapped_column(Boolean)]
    datetime = Annotated[datetime, mapped_column(String(60))]
    str_20 = Annotated[str, mapped_column(String(20))]
    str_50 = Annotated[str, mapped_column(String(50))]
    str_100 = Annotated[str, mapped_column(String(100))]
    optional_str_200 = Annotated[Optional[str], mapped_column(String(200), nullable=True)]
    