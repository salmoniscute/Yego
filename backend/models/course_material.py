from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import BaseType
from models.component import Component

class CourseMaterial(Component):
    __tablename__ = "CourseMaterial"
    id: Mapped[BaseType.int_id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
    course_id: Mapped[BaseType.str_20] = mapped_column(ForeignKey("Course.id", ondelete="CASCADE"))

    # Relationship to parent
    info: Mapped["Component"] = relationship("Component", back_populates="course_materials")
    course_info: Mapped["Course"] = relationship("Course", back_populates="course_materials")

    def __init__(self, uid: str, course_id: str, release_time: str, title: str, content: str) -> None:
        self.uid = uid
        self.course_id = course_id
        self.release_time = release_time
        self.title = title
        self.content = content

    def __repr__(self) -> str:
        return f"CourseMaterial(id={self.id}, uid={self.uid}, course_id={self.course_id}, release_time={self.release_time}, title={self.title}, content={self.content})"