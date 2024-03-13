from typing import Optional 
from sqlalchemy.orm import Mapped, relationship
from models.base import Base, BaseType

class Discussion(Base):
    __tablename__ = "Discussion"
    discussion_id : Mapped[BaseType.discussion_id]
    course_id : Mapped[BaseType.str_20]
    title : Mapped[BaseType.str_100]
    discription : Mapped[BaseType.str_100]


    def __init__(self,discussion_id:str, course_id:str, title:float, discription:str) -> None:
        self.discussion_id = discussion_id
        self.course_id = course_id
        self.title = title
        self.discription = discription

    def __repr__(self) -> str:
        return f"Course(discussion_id={self.discussion_id}, course_id={self.course_id}, title={self.title}, discription={self.discription})"

