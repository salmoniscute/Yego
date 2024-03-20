from typing import Optional 
from sqlalchemy.orm import Mapped, relationship
from models.base import Base, BaseType

class DiscussionTopic(Base):
    __tablename__ = "DiscussionTopic"
    topic_id : Mapped[BaseType.topic_id]
    discussion_id : Mapped[BaseType.str_20]
    publisher : Mapped[BaseType.str_20]
    title : Mapped[BaseType.str_100]
    release_time : Mapped[BaseType.str_20]
    content : Mapped[BaseType.str_100]


    def __init__(self,topic_id:str, discussion_id:str, publisher:str, title:str, release_time:str, content:str) -> None:
        self.topic_id = topic_id
        self.discussion_id = discussion_id
        self.publisher = publisher
        self.title = title
        self.release_time = release_time
        self.content = content

    def __repr__(self) -> str:
        return f"DiscussionTopic(topic_id={self.topic_id}, discussion_id={self.discussion_id}, publisher={self.publisher}, title={self.title}, release_time={self.release_time}, content={self.content})"

