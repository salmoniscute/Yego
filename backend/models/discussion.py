from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, BaseType
from models.component import Component


class Discussion(Base):
    __tablename__ = "Discussion"
    id: Mapped[BaseType.component_id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
    course_id: Mapped[BaseType.str_10] = mapped_column(ForeignKey("Course.id", ondelete="CASCADE"))

    # Relationship to parent
    info: Mapped["Component"] = relationship("Component",back_populates="discussion")

    course_info: Mapped["Course"] = relationship(
        "Course",
        back_populates="discussions",
        lazy="joined"
    )

    def __init__(self, id: int, course_id:str) -> None:
        self.id = id
        self.course_id = course_id
        

    def __repr__(self) -> str:
        return f"Discussion(id={self.id}, course_id={self.course_id})"


class DiscussionTopic(Base):
    __tablename__ = "DiscussionTopic"
    id: Mapped[BaseType.component_id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
    discussion_id: Mapped[BaseType.int_type] = mapped_column(ForeignKey("Discussion.id", ondelete="CASCADE"))

    # Relationship to parent
    info: Mapped["Component"] = relationship("Component",back_populates="topic")

    def __init__(self, id: int, discussion_id: int) -> None:
        self.id = id
        self.discussion_id = discussion_id

    def __repr__(self) -> str:
        return f"DiscussionTopic(id={self.id}, discussion_id={self.discussion_id})"


class DiscussionTopicReply(Base):
    __tablename__ = "DiscussionTopicReply"
    id: Mapped[BaseType.component_id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
    root_id: Mapped[BaseType.int_type] = mapped_column(ForeignKey("DiscussionTopic.id", ondelete="CASCADE"))
    parent_id: Mapped[BaseType.int_type]
    
    info: Mapped["Component"] = relationship("Component", back_populates="discussion_reply")
    
    def __init__(self, id: str, root_id: int, parent_id: int) -> None:
        self.id = id
        self.root_id = root_id
        self.parent_id = parent_id
        
    def __repr__(self) -> str:
        return f"DiscussionTopicReply(id={self.id}, root_id={self.root_id}, parent={self.parent_id})"
