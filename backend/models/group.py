from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, BaseType


class Group(Base):
    __tablename__ = "Group"
    id: Mapped[BaseType.int_id]
    course_id: Mapped[BaseType.str_20] = mapped_column(ForeignKey("Course.id", ondelete="CASCADE"))
    name: Mapped[BaseType.str_20]

    # Relationship to parent
    course_info: Mapped["Course"] = relationship("Course", back_populates="groups")

    def __init__(self, course_id: str, name: str) -> None:
        self.course_id = course_id
        self.name = name

    def __repr__(self) -> str:
        return f"Group(id={self.id}, course_id={self.course_id}, name={self.name})"
    