from typing import Optional 
from sqlalchemy.orm import Mapped, relationship
from models.base import Base, BaseType
from datetime import datetime

class Course_bulletin(Base):
    __tablename__ = "Course bulletin"
    cb_id : Mapped[BaseType.cb_id]
    publisher: Mapped[BaseType.str_20]
    course_id: Mapped[BaseType.str_20]
    title: Mapped[BaseType.str_20]
    release_time: Mapped[BaseType.str_20] #Mapped[BaseType.datetime]
    content: Mapped[BaseType.str_20]


    def __init__(self,cb_id:str, publisher:str, course_id:str, title:str, release_time:str, content:str) -> None:
        self.cb_id = cb_id 
        self.publisher = publisher
        self.course_id = course_id
        self.title = title
        self.release_time = release_time
        self.content = content
        

    def __repr__(self) -> str:
        return f"Course bulletin(cb_id={self.cb_id}, publisher={self.publisher}, course_id={self.course_id}, title={self.title}, release_time={self.release_time}, content={self.content})"

