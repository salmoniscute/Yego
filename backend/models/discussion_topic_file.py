from typing import Optional 
from sqlalchemy.orm import Mapped, relationship
from models.base import Base, BaseType

class Discussion_topic_file(Base):
    __tablename__ = "DiscussionTopicFile"
    file_id : Mapped[BaseType.file_id]
    topic_id : Mapped[BaseType.str_20]
    path : Mapped[BaseType.str_100]


    def __init__(self,file_id:str, topic_id:str, path:str) -> None:
        self.file_id = file_id
        self.topic_id = topic_id
        self.path = path

    def __repr__(self) -> str:
        return f"DiscussionTopicFile(file_id={self.file_id}, topic_id={self.topic_id}, path={self.path})"

