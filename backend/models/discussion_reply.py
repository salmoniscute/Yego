from typing import Optional 
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey
from models.base import Base, BaseType

class DiscussionReply(Base):
    __tablename__ = "DiscussionReply"
    reply_id : Mapped[BaseType.reply_id]
    # topic_id : Mapped[BaseType.str_20]
    # publisher : Mapped[BaseType.str_20]
    release_time : Mapped[BaseType.str_20]
    content : Mapped[BaseType.str_100]
    parent : Mapped[BaseType.str_20]
    
    # relationship to DiscussionTopic child to parent
    topic_id : Mapped[BaseType.str_20] = mapped_column(ForeignKey("DiscussionTopic.topic_id", ondelete="CASCADE"))
    topic : Mapped["DiscussionTopic"] = relationship(
        "DiscussionTopic", 
        back_populates="replies"
    )
    
    # relationship to User child to parent
    publisher : Mapped[BaseType.str_20] = mapped_column(ForeignKey("User.uid", ondelete="CASCADE"))
    publisher_info : Mapped["User"] = relationship(
        "User", 
        back_populates="replies"
    )


    def __init__(self, reply_id:str, topic_id:str, publisher:str, release_time:str, content:str, parent: str) -> None:
        self.reply_id = reply_id
        self.topic_id = topic_id        
        self.publisher = publisher
        self.release_time = release_time
        self.content = content
        self.parent = parent

    def __repr__(self) -> str:
        return f"DiscussionReply(reply_id={self.reply_id}, topic_id={self.topic_id}, publisher={self.publisher}, release_time={self.release_time}, content={self.content}, parent={self.parent})"

