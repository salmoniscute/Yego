from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, BaseType


class Group(Base):
    __tablename__ = "Group"
    id: Mapped[BaseType.group_id]
    course_id: Mapped[BaseType.str_10] = mapped_column(ForeignKey("Course.id", ondelete="CASCADE"))
    name: Mapped[BaseType.str_20]
    number_of_members: Mapped[BaseType.int_type]
    create_deadline: Mapped[BaseType.datetime]

    # Relationship to parent
    course_info: Mapped["Course"] = relationship("Course", back_populates="groups")

    # Relationship to child
    members: Mapped[list["SelectedCourse"]] = relationship(
        "SelectedCourse", 
        back_populates="group_info"
    )

    def __init__(self, course_id: str, name: str, number_of_members: int, create_deadline: str) -> None:
        self.course_id = course_id
        self.name = name
        self.number_of_members = number_of_members
        self.create_deadline = create_deadline

    def __repr__(self) -> str:
        return f"Group(id={self.id}, course_id={self.course_id}, name={self.name}, number_of_members={self.number_of_members}, create_deadline={self.create_deadline})"
    