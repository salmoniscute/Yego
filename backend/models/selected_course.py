from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional 

from models.base import Base, BaseType


class SelectedCourse(Base):
    __tablename__ = "SelectedCourse"
    id: Mapped[BaseType.int_id]
    uid: Mapped[BaseType.str_20] = mapped_column(ForeignKey("User.uid", ondelete="CASCADE"))
    course_id: Mapped[BaseType.str_20] = mapped_column(ForeignKey("Course.id", ondelete="CASCADE"))
    group_id: Mapped[BaseType.int_type] = mapped_column(ForeignKey("Group.id"), nullable=True)

    # Relationship to parent
    user_info: Mapped["User"] = relationship("User", back_populates="selected_courses", lazy="joined")
    course_info: Mapped["Course"] = relationship("Course", back_populates="selected_courses", lazy="joined")
    group_info: Mapped["Group"] = relationship("Group", back_populates="members")

    def __init__(self, uid: str, course_id: str, group_id: Optional[int] = None) -> None:
        self.uid = uid
        self.course_id = course_id
        self.group_id = group_id

    def __repr__(self) -> str:
        return f"SelectedCourse(id={self.id}, uid={self.uid}, course_id={self.course_id}, group_id={self.group_id})"
    