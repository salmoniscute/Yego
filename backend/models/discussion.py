from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from typing import Optional 

from models.base import Base, BaseType
from models.component import Component


class Discussion(Component):
    __tablename__ = "Discussion"
    id: Mapped[BaseType.id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
    course_id: Mapped[BaseType.str_20] = mapped_column(ForeignKey("Course.id", ondelete="CASCADE"), nullable=True)

    # Relationship to parent
    info: Mapped["Component"] = relationship(
        "Component",
        back_populates="discussions",
        lazy="joined"
    )

    course_info: Mapped["Course"] = relationship(
        "Course",
        back_populates="discussions"
    )

    def __init__(self, id: str, uid: str, course_id: str, release_time: str, title: str, content: str) -> None:
        self.id = id
        self.uid = uid
        self.course_id = course_id
        self.release_time = release_time
        self.title = title
        self.content = content

    def __repr__(self) -> str:
        return f"Discussion(id={self.id}, uid={self.uid}, course_id={self.course_id}, release_time={self.release_time}, title={self.title}, content={self.content})"
    