from sqlalchemy.orm import Mapped, relationship
from typing import Optional 

from models.base import Base, BaseType
from models.selected_course import SelectedCourse


class User(Base):
    __tablename__ = "User"
    uid: Mapped[BaseType.id]
    password: Mapped[BaseType.hashed_password]
    name: Mapped[BaseType.str_20]
    role: Mapped[BaseType.str_20]
    email: Mapped[BaseType.str_50]
    department: Mapped[BaseType.str_20]
    country: Mapped[BaseType.str_20]
    introduction: Mapped[BaseType.optional_str_200]
    avatar: Mapped[BaseType.optional_str_200]

    # Relationship to child
    courses: Mapped[list["Course"]] = relationship(
        "Course",
        back_populates="instructor_info",
        cascade="all, delete-orphan",
        passive_deletes=True,
        lazy="joined"
    )

    selected_courses: Mapped[list["SelectedCourse"]] = relationship(
        "SelectedCourse",
        back_populates="user_info",
        cascade="all, delete-orphan", 
        passive_deletes=True,
        lazy="joined"
    )

    publications: Mapped[list["Component"]] = relationship(
        "Component",
        back_populates="publisher_info",
        cascade="all, delete-orphan",
        passive_deletes=True,
        lazy="joined"
    )

    files: Mapped[list["File"]] = relationship(
        "File",
        back_populates="owner_info",
        cascade="all, delete-orphan",
        passive_deletes=True,
        lazy="joined"
    )

    def __init__(self, uid: str, password: str, name: str, role: str, email: str, department: str, country: str, introduction: Optional[str], avatar: Optional[str]) -> None:
        self.uid = uid
        self.password = password
        self.name = name
        self.role = role
        self.email = email
        self.department = department
        self.country = country
        self.introduction = introduction
        self.avatar = avatar

    def __repr__(self) -> str:
        return f"User(uid={self.uid}, password={self.password}, name={self.name}, role={self.role}, email={self.email}, department={self.department}, country={self.country}, introduction={self.introduction}, avatat={self.avatar})"
    