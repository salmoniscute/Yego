from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional 

from models.base import Base, BaseType


class SelectedCourse(Base):
    __tablename__ = "SelectedCourse"
    uid: Mapped[BaseType.id] = mapped_column(ForeignKey("User.uid", ondelete="CASCADE"))
    course_id: Mapped[BaseType.id] = mapped_column(ForeignKey("Course.id", ondelete="CASCADE"))
    group: Mapped[BaseType.optional_str_200]

    # Relationship to parent
    user_info: Mapped["User"] = relationship(
        "User",
        back_populates="selected_courses",
        lazy="joined"
    )
    
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
    