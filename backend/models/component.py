from typing import Optional 
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey
from models.base import Base, BaseType


class Component(Base):
    __tablename__ = "Component"
    id: Mapped[BaseType.id]
    publisher: Mapped[BaseType.str_20] = mapped_column(ForeignKey("User.uid", ondelete="CASCADE"))
    release_time: Mapped[BaseType.datetime]
    title: Mapped[BaseType.str_100]
    content: Mapped[BaseType.str_100]

    # Relationship to parent
    publisher_info: Mapped["User"] = relationship(
        "User",
        back_populates="publications",
        lazy="joined"
    )

    # Relationship to child
    # course_bulletins: Mapped[list["CourseBulletin"]] = relationship(
    #     "CourseBulletin",
    #     back_populates="info",
    #     cascade="all, delete-orphan", 
    #     passive_deletes=True,
    #     lazy="joined"
    # )

    # website_bulletins: Mapped[list["WebsiteBulletin"]] = relationship(
    #     "WebsiteBulletin",
    #     back_populates="info",
    #     cascade="all, delete-orphan", 
    #     passive_deletes=True,
    #     lazy="joined"
    # )

    files: Mapped[list["File"]] = relationship(
        "File",
        back_populates="component_info",
        cascade="all, delete-orphan",
        passive_deletes=True,
        lazy="joined"
    )

    def __init__(self, id: str, publisher: str, release_time: str, title: str, content: str) -> None:
        self.id = id
        self.publisher = publisher
        self.release_time = release_time
        self.title = title
        self.content = content

    def __repr__(self) -> str:
        return f"Component(id={self.id}, publisher={self.publisher}, release_time={self.release_time}, title={self.title}, content={self.content})"
