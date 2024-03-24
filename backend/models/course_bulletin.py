from typing import Optional 
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey
from models.base import Base, BaseType


class CourseBulletin(Base):
    __tablename__ = "CourseBulletin"
    cb_id : Mapped[BaseType.cb_id]
    publisher: Mapped[BaseType.str_20]
    title: Mapped[BaseType.str_100]
    release_time: Mapped[BaseType.str_100] #Mapped[BaseType.datetime]
    content: Mapped[BaseType.str_100]
    pin_to_top: Mapped[BaseType.boolean]
    
    
    #relationship to CourseBulletinFile parent to child
    files : Mapped["CourseBulletinFile"] = relationship(
        "CourseBulletinFile", 
        back_populates="course_bulletin",
        cascade="all, delete, delete-orphan",
        passive_deletes=True,
        lazy="joined"
    )
    
    #relationship to Course child to parent
    course_id : Mapped[BaseType.str_20] = mapped_column(ForeignKey("Course.course_id", ondelete="CASCADE"))
    course : Mapped["Course"] = relationship(
        "Course", 
        back_populates="bulletins"
    )


    def __init__(self,cb_id:str, publisher:str, course_id:str, title:str, release_time:str, content:str, pin_to_top:bool) -> None:
        self.cb_id = cb_id 
        self.publisher = publisher
        self.course_id = course_id
        self.title = title
        self.release_time = release_time
        self.content = content
        self.pin_to_top = pin_to_top
        

    def __repr__(self) -> str:
        return f"Course bulletin(cb_id={self.cb_id}, publisher={self.publisher}, course_id={self.course_id}, title={self.title}, release_time={self.release_time}, content={self.content}, pin_to_top={self.pin_to_top})"

