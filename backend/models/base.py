from datetime import datetime
from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import DeclarativeBase, mapped_column
from typing import Annotated, Optional


class Base(DeclarativeBase):
    pass


class BaseType:
    uid = Annotated[int, mapped_column(String(10), primary_key=True, unique=True)]
    component_id = Annotated[int, mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)]
    file_id = Annotated[int, mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)]
    course_id = Annotated[int, mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)]
    selected_course_id = Annotated[int, mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)]
    group_id = Annotated[int, mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)]
    notification_id = Annotated[int, mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)]
    subscription_id = Annotated[int, mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)]

    hashed_password = Annotated[str, mapped_column(String(60))]
    boolean = Annotated[bool, mapped_column(Boolean)]
    int_type = Annotated[int, mapped_column(Integer)]
    str_10 = Annotated[str, mapped_column(String(10))]
    str_20 = Annotated[str, mapped_column(String(20))]
    str_50 = Annotated[str, mapped_column(String(50))]
    str_100 = Annotated[str, mapped_column(String(100))]
    str_1000 = Annotated[str, mapped_column(String(1000))]
    optional_str_200 = Annotated[Optional[str], mapped_column(String(200), nullable=True)]
    optional_str_1000 = Annotated[Optional[str], mapped_column(String(1000), nullable=True)]
    datetime = Annotated[datetime, mapped_column(String(60), nullable=True)]
    path = Annotated[str, mapped_column(String(1000), nullable=True)]