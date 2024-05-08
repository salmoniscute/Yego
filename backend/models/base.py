from datetime import datetime
from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import DeclarativeBase, mapped_column
from typing import Annotated, Optional


class Base(DeclarativeBase):
    pass


class BaseType:
    id = Annotated[int, mapped_column(String(10), primary_key=True, unique=True)]
    int_id = Annotated[int, mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)]
    group_id = Annotated[int, mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)]
    hashed_password = Annotated[str, mapped_column(String(60))]
    boolean = Annotated[bool, mapped_column(Boolean)]
    datetime = Annotated[datetime, mapped_column(String(60), nullable=True)]
    str_20 = Annotated[str, mapped_column(String(20))]
    str_50 = Annotated[str, mapped_column(String(50))]
    str_100 = Annotated[str, mapped_column(String(100))]
    optional_str_200 = Annotated[Optional[str], mapped_column(String(200), nullable=True)]
    int_type = Annotated[int, mapped_column(Integer)]
    