from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, BaseType


class Component(Base):
    __tablename__ = "Component"
    id: Mapped[BaseType.int_id]
    uid: Mapped[BaseType.str_20] = mapped_column(ForeignKey("User.uid", ondelete="CASCADE"))
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
    course_bulletin: Mapped["CourseBulletin"] = relationship(
        "CourseBulletin",
        back_populates="info",
        cascade="all, delete-orphan", 
        passive_deletes=True
    )

    website_bulletin: Mapped["WebsiteBulletin"] = relationship(
        "WebsiteBulletin",
        back_populates="info",
        cascade="all, delete-orphan", 
        passive_deletes=True
    )

    discussions: Mapped[list["Discussion"]] = relationship(
        "Discussion",
        back_populates="info",
        cascade="all, delete-orphan", 
        passive_deletes=True
    )

    topics: Mapped[list["DiscussionTopic"]] = relationship(
        "DiscussionTopic",
        back_populates="info",
        cascade="all, delete-orphan", 
        passive_deletes=True
    )

    files: Mapped[list["File"]] = relationship(
        "File",
        back_populates="component_info",
        cascade="all, delete-orphan",
        passive_deletes=True,
        lazy="selectin"
    )

    subscriptions: Mapped[list["Subscription"]] = relationship(
        "Subscription",
        back_populates="component_info",
        cascade="all, delete-orphan",
        passive_deletes=True,
        lazy="selectin"
    )

    notifications: Mapped[list["Notification"]] = relationship(
        "Notification",
        back_populates="component_info",
        cascade="all, delete-orphan",
        passive_deletes=True
    )
    
    reports: Mapped[list["Report"]] = relationship(
        "Report",
        back_populates="info",
        cascade="all, delete-orphan", 
        passive_deletes=True
    )
    
    course_materials: Mapped[list["CourseMaterial"]] = relationship(
        "CourseMaterial",
        back_populates="info",
        cascade="all, delete-orphan", 
        passive_deletes=True
    )

    def __init__(self, uid: str, release_time: str, title: str, content: str) -> None:
        self.uid = uid
        self.release_time = release_time
        self.title = title
        self.content = content

    def __repr__(self) -> str:
        return f"Component(id={self.id}, uid={self.uid}, release_time={self.release_time}, title={self.title}, content={self.content})"
