from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional 

from models.base import Base, BaseType


class SelectedCourse(Base):
    __tablename__ = "SelectedCourse"
    group: Mapped[BaseType.optional_str_200]

    # relationship to parent
    uid: Mapped[BaseType.uid] = mapped_column(ForeignKey("User.uid", ondelete="CASCADE"))
    student_info: Mapped["User"] = relationship(
        "User",
        back_populates="selected_courses",
        lazy="joined"
    )

    course_id: Mapped[BaseType.course_id] = mapped_column(ForeignKey("Course.course_id", ondelete="CASCADE"))
    course_info: Mapped["Course"] = relationship(
        "Course",
        back_populates="selected_courses",
        lazy="joined"
    )

    def __init__(self, uid: str, course_id: str, group: Optional[str]) -> None:
        self.uid = uid
        self.course_id = course_id
        self.group = group

    def __repr__(self) -> str:
        return f"User(uid={self.uid}, course_id={self.course_id}, group={self.group})"
    