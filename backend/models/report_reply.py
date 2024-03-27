from typing import Optional 
from sqlalchemy.orm import Mapped, relationship
from models.base import Base, BaseType

class ReportReply(Base):
    __tablename__ = "ReportReply"
    reply_id : Mapped[BaseType.reply_id]
    parent: Mapped[BaseType.str_20]
    report_id : Mapped[BaseType.str_20]
    publisher : Mapped[BaseType.str_20]
    release_time : Mapped[BaseType.str_20]
    content : Mapped[BaseType.str_100]


    def __init__(self, reply_id:str, parent:str, report_id:str, publisher:str, release_time:str, content:str) -> None:
        self.reply_id = reply_id
        self.parent = parent
        self.report_id = report_id        
        self.publisher = publisher
        self.release_time = release_time
        self.content = content

    def __repr__(self) -> str:
        return f"ReportReply(reply_id={self.reply_id}, parent={self.parent}, report_id={self.report_id}, publisher={self.publisher}, release_time={self.release_time}, content={self.content})"

