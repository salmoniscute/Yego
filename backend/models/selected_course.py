from sqlalchemy.orm import Mapped, relationship
from typing import Optional 

from models.base import Base, BaseType


class SelectedCourse(Base):
    __tablename__ = "SelectedCourse"
    uid: Mapped[BaseType.uid]
    course_id: Mapped[BaseType.course_id]
    group: Mapped[BaseType.optional_str_200]

    def __init__(self, uid: str, course_id: str, group: Optional[str]) -> None:
        self.uid = uid
        self.course_id = course_id
        self.group = group

    def __repr__(self) -> str:
        return f"User(uid={self.uid}, course_id={self.course_id}, group={self.group})"
    