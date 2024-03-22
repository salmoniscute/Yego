from typing import Optional 
from sqlalchemy.orm import Mapped, relationship
from models.base import Base, BaseType

class Course(Base):
    __tablename__ = "Course"
    course_id : Mapped[BaseType.course_id]
    teacher : Mapped[BaseType.str_20]
    course_code : Mapped[BaseType.str_20]
    academic_year : Mapped[BaseType.str_20]
    semester : Mapped[int]
    name : Mapped[BaseType.str_100]
    outline : Mapped[BaseType.str_100]
    
    #relationship to CourseBulletin parent to child
    bulletins : Mapped[list["CourseBulletin"]] = relationship(
        "CourseBulletin",
        back_populates="course",
        cascade="all, delete, delete-orphan",
        passive_deletes=True,
        lazy="joined"
    )
    
    #relationship to Discussion parent to child
    discussions : Mapped[list["Discussion"]] = relationship(
        "Discussion",
        back_populates="course",
        cascade="all, delete, delete-orphan",
        passive_deletes=True,
        lazy="joined"
    )


    def __init__(self,course_id:str, teacher:str, course_code:float, academic_year:int, semester:int, name:str, outline:Optional[str]) -> None:
        self.course_id = course_id
        self.teacher = teacher
        self.course_code = course_code
        self.academic_year = academic_year
        self.semester = semester
        self.name = name
        self.outline = outline

    def __repr__(self) -> str:
        return f"Course(course_id={self.course_id}, teacher={self.teacher}, course_code={self.course_code}, academic_year={self.academic_year}, semester={self.semester}), name={self.name}, outline={self.outline})"

