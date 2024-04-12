from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, BaseType
from models.component import Component


class Discussion(Component):
    __tablename__ = "Discussion"
    id: Mapped[BaseType.int_id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
    course_id: Mapped[BaseType.str_20] = mapped_column(ForeignKey("Course.id", ondelete="CASCADE"))

    # Relationship to parent
    info: Mapped["Component"] = relationship(
        "Component",
        back_populates="discussions"
    )

    course_info: Mapped["Course"] = relationship(
        "Course",
        back_populates="discussions"
    )

    # Relationship to child
    # topics: Mapped[list["DiscussionTopic"]] = relationship(
    #     "DiscussionTopic",
    #     back_populates="discussion_info",
    #     cascade="all, delete-orphan",
    #     passive_deletes=True
    # )

    def __init__(self, uid: str, course_id: str, release_time: str, title: str, content: str) -> None:
        self.uid = uid
        self.course_id = course_id
        self.release_time = release_time
        self.title = title
        self.content = content

    def __repr__(self) -> str:
        return f"Discussion(id={self.id}, uid={self.uid}, course_id={self.course_id}, release_time={self.release_time}, title={self.title}, content={self.content})"


class DiscussionTopic(Component):
    __tablename__ = "DiscussionTopic"
    id: Mapped[BaseType.int_id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
    # discussion_id: Mapped[BaseType.str_20] = mapped_column(ForeignKey("Discussion.id", ondelete="CASCADE"))
    type: Mapped[BaseType.str_100]

    # Relationship to parent
    info: Mapped["Component"] = relationship(
        "Component",
        back_populates="topics"
    )

    # discussion_info: Mapped["Discussion"] = relationship(
    #     "Discussion",
    #     back_populates="topics",
    # )

    __mapper_args__ = {
        "polymorphic_identity": "topic",
        "polymorphic_on": "type"
    }

    def __init__(self, uid: str, discussion_id: str, release_time: str, title: str, content: str) -> None:
        self.uid = uid
        self.discussion_id = discussion_id
        self.release_time = release_time
        self.title = title
        self.content = content

    def __repr__(self) -> str:
        return f"DiscussionTopic(id={self.id}, uid={self.uid}, discussion_id={self.discussion_id}, release_time={self.release_time}, title={self.title}, content={self.content})"


class DiscussionTopicReply(DiscussionTopic):
    # parent_id: Mapped[BaseType.str_20] = mapped_column(ForeignKey("DiscussionTopic.id", ondelete="CASCADE"), nullable=True)
    # root_id: Mapped[BaseType.str_20] = mapped_column(ForeignKey("DiscussionTopic.id", ondelete="CASCADE"), nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "reply",
    }
