from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, BaseType


class Component(Base):
    __tablename__ = "Component"
    id: Mapped[BaseType.component_id]
    uid: Mapped[BaseType.str_10] = mapped_column(ForeignKey("User.uid", ondelete="CASCADE"))
    release_time: Mapped[BaseType.datetime]
    title: Mapped[BaseType.str_100]
    content: Mapped[BaseType.str_1000]

    # Relationship to parent
    publisher_info: Mapped["User"] = relationship("User", back_populates="publications", lazy="joined")

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

    discussion: Mapped["Discussion"] = relationship(
        "Discussion",
        back_populates="info",
        cascade="all, delete-orphan", 
        passive_deletes=True
    )

    topic: Mapped["DiscussionTopic"] = relationship(
        "DiscussionTopic",
        back_populates="info",
        cascade="all, delete-orphan", 
        passive_deletes=True
    )
    
    discussion_reply: Mapped["DiscussionTopicReply"] = relationship(
        "DiscussionTopicReply",
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
    
    report: Mapped["Report"] = relationship(
        "Report",
        back_populates="info",
        cascade="all, delete-orphan", 
        passive_deletes=True
    )

    reply: Mapped["ReportReply"] = relationship(
        "ReportReply",
        back_populates="info",
        cascade="all, delete-orphan", 
        passive_deletes=True
    )
    
    course_material: Mapped["CourseMaterial"] = relationship(
        "CourseMaterial",
        back_populates="info",
        cascade="all, delete-orphan",
        passive_deletes=True
    )
    
    material_info: Mapped["MaterialInfo"] = relationship(
        "MaterialInfo",
        back_populates="info",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    assignment: Mapped["Assignment"] = relationship(
        "Assignment",
        back_populates="info",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    def __init__(self, uid: str, title: str, content: str, release_time: str) -> None:
        self.uid = uid
        self.release_time = release_time
        self.title = title
        self.content = content

    def __repr__(self) -> str:
        return f"Component(id={self.id}, uid={self.uid}, release_time={self.release_time}, title={self.title}, content={self.content})"
