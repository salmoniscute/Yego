from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey
from typing import Optional 

from models.base import Base, BaseType


class Course(Base):
    __tablename__ = "Course"
    id: Mapped[BaseType.id]
    instructor: Mapped[BaseType.str_20] = mapped_column(ForeignKey("User.uid", ondelete="CASCADE"))
    course_code: Mapped[BaseType.str_20]
    academic_year: Mapped[BaseType.str_20]
    semester: Mapped[int]
    name: Mapped[BaseType.str_100]
    outline: Mapped[BaseType.str_100]

    # Relationship to parent
    instructor_info: Mapped["User"] = relationship(
        "User",
        back_populates="courses",
        lazy="joined"
    )

    # Relationship to child
    selected_courses: Mapped[list["SelectedCourse"]] = relationship(
        "SelectedCourse",
        back_populates="course_info",
        cascade="all, delete-orphan", 
        passive_deletes=True,
        lazy="joined"
    )

    bulletins: Mapped[list["Bulletin"]] = relationship(
        "Bulletin",
        back_populates="course_info",
        cascade="all, delete-orphan", 
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

