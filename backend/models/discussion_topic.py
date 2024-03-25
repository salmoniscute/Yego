from typing import Optional 
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey
from models.base import Base, BaseType

class DiscussionTopic(Base):
    __tablename__ = "DiscussionTopic"
    topic_id : Mapped[BaseType.topic_id]
    # discussion_id : Mapped[BaseType.str_20]
    # publisher : Mapped[BaseType.str_20]
    title : Mapped[BaseType.str_100]
    release_time : Mapped[BaseType.str_20]
    content : Mapped[BaseType.str_100]
    
    # relationship to DiscussionTopicFile parent to child
    files : Mapped[list["DiscussionTopicFile"]] = relationship(
        "DiscussionTopicFile",
        back_populates="topic",
        cascade="all, delete, delete-orphan",
        passive_deletes=True,
        lazy="joined"
    )
    
    # relationship to DiscussionReply parent to child
    replies : Mapped[list["DiscussionReply"]] = relationship(
        "DiscussionReply",
        back_populates="topic",
        cascade="all, delete, delete-orphan",
        passive_deletes=True,
        lazy="joined"
    )
    
    # relationship to Discussion child to parent
    discussion_id : Mapped[BaseType.str_20] = mapped_column(ForeignKey("Discussion.discussion_id", ondelete="CASCADE"))
    discussion : Mapped["Discussion"] = relationship(
        "Discussion", 
        back_populates="topics"
    )
    
    # relationship to User child to parent
    publisher : Mapped[BaseType.str_20] = mapped_column(ForeignKey("User.uid", ondelete="CASCADE"))
    publisher_info : Mapped["User"] = relationship(
        "User", 
        back_populates="topics"
    )


    def __init__(self,topic_id:str, discussion_id:str, publisher:str, title:str, release_time:str, content:str) -> None:
        self.topic_id = topic_id
        self.discussion_id = discussion_id
        self.publisher = publisher
        self.title = title
        self.release_time = release_time
        self.content = content

    def __repr__(self) -> str:
        return f"DiscussionTopic(topic_id={self.topic_id}, discussion_id={self.discussion_id}, publisher={self.publisher}, title={self.title}, release_time={self.release_time}, content={self.content})"

