from sqlalchemy import String, DateTime, Boolean, String
from sqlalchemy.orm import DeclarativeBase, mapped_column
from typing import Annotated, Optional
from datetime import datetime

class Base(DeclarativeBase):
    pass


class BaseType:
    hashed_password = Annotated[str, mapped_column(String(60))]
    boolean = Annotated[bool, mapped_column(Boolean)]
    str_20 = Annotated[str, mapped_column(String(20))]
    str_50 = Annotated[str, mapped_column(String(50))]
    str_100 = Annotated[str, mapped_column(String(100))]
    optional_str_200 = Annotated[Optional[str], mapped_column(String(200), nullable=True)]
    
    uid = Annotated[int, mapped_column(String(10), primary_key=True)]
    course_id = Annotated[str, mapped_column(String(10), primary_key=True)]
    wb_id = Annotated[str, mapped_column(String(10), primary_key=True)]
    wb_file_id = Annotated[str, mapped_column(String(10), primary_key=True)]
    
    cb_id = Annotated[str, mapped_column(String(10), primary_key=True)]
    datetime = Annotated[datetime, mapped_column(DateTime)] #jwt problem
    
    discussion_id = Annotated[str, mapped_column(String(10), primary_key=True)]
    
    topic_id = Annotated[str, mapped_column(String(10), primary_key=True)]
    
    reply_id = Annotated[str, mapped_column(String(10), primary_key=True)]
    
    file_id = Annotated[str, mapped_column(String(10), primary_key=True)]