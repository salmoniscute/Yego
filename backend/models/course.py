from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional 

from models.base import Base, BaseType


class Course(Base):
    __tablename__ = "Course"
    id: Mapped[BaseType.course_id]
    uid: Mapped[BaseType.str_10] = mapped_column(ForeignKey("User.uid", ondelete="CASCADE"))
    course_code: Mapped[BaseType.str_10]
    academic_year: Mapped[BaseType.int_type]
    semester: Mapped[BaseType.int_type]
    name: Mapped[BaseType.str_50]
    outline: Mapped[BaseType.str_1000]

    # Relationship to parent
    instructor_info: Mapped["User"] = relationship("User", back_populates="courses", lazy="joined")

    # Relationship to child
    selected_courses: Mapped[list["SelectedCourse"]] = relationship(
        "SelectedCourse",
        back_populates="course_info",
        cascade="all, delete-orphan", 
        passive_deletes=True
    )

    groups: Mapped[list["Group"]] = relationship(
        "Group",
        back_populates="course_info",
        cascade="all, delete-orphan", 
        passive_deletes=True
    )

    course_bulletins: Mapped[list["CourseBulletin"]] = relationship(
        "CourseBulletin",
        back_populates="course_info",
        cascade="all, delete-orphan", 
        passive_deletes=True
    )

    discussions: Mapped[list["Discussion"]] = relationship(
        "Discussion",
        back_populates="course_info",
        cascade="all, delete-orphan", 
        passive_deletes=True,
        lazy="selectin"
    )
    
    course_materials: Mapped[list["CourseMaterial"]] = relationship(
        "CourseMaterial",
        back_populates="course_info",
        cascade="all, delete-orphan", 
        passive_deletes=True
    )

    def __init__(self, id: int, uid: str, course_code: float, academic_year: int, semester: int, name: str, outline: Optional[str]) -> None:
        self.id = id
        self.uid = uid
        self.course_code = course_code
        self.academic_year = academic_year
        self.semester = semester
        self.name = name
        self.outline = outline

    def __repr__(self) -> str:
        return f"Course(id={self.id}, uid={self.uid}, course_code={self.course_code}, academic_year={self.academic_year}, semester={self.semester}, name={self.name}, outline={self.outline})"
