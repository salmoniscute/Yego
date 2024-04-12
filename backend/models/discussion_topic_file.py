from typing import Optional 
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey
from models.base import Base, BaseType

class DiscussionTopicFile(Base):
    __tablename__ = "DiscussionTopicFile"
    file_id : Mapped[BaseType.file_id]
    path : Mapped[BaseType.str_100]
    
    # relationship to parent
    topic_id : Mapped[BaseType.str_20] = mapped_column(ForeignKey("DiscussionTopic.topic_id", ondelete="CASCADE"))
    topic : Mapped["DiscussionTopic"] = relationship(
        "DiscussionTopic", 
        back_populates="files"
    )


    def __init__(self,file_id:str, topic_id:str, path:str) -> None:
        self.file_id = file_id
        self.topic_id = topic_id
        self.path = path

    def __repr__(self) -> str:
        return f"DiscussionTopicFile(file_id={self.file_id}, topic_id={self.topic_id}, path={self.path})"

