from typing import Optional
from sqlalchemy import ForeignKey 
from sqlalchemy.orm import Mapped, relationship, mapped_column
from models.base import Base, BaseType

class ReportReply(Base):
    __tablename__ = "ReportReply"
    reply_id : Mapped[BaseType.reply_id]
    parent: Mapped[Optional[BaseType.str_20]]
    # report_id : Mapped[BaseType.str_20]
    publisher : Mapped[BaseType.str_20]
    release_time : Mapped[BaseType.str_20]
    content : Mapped[BaseType.str_100]

    # relationship to Discussion child to parent
    report_id : Mapped[BaseType.str_20] = mapped_column(ForeignKey("Report.report_id", ondelete="CASCADE"))
    report : Mapped["Report"] = relationship(
        "Report", 
        back_populates="replies"
    )
    
    # relationship to User child to parent
    publisher : Mapped[BaseType.str_20] = mapped_column(ForeignKey("User.uid", ondelete="CASCADE"))
    publisher_info : Mapped["User"] = relationship(
        "User", 
        back_populates="report_replies"
    )

    def __init__(self, reply_id:str, parent:Optional[str], report_id:str, publisher:str, release_time:str, content:str) -> None:
        self.reply_id = reply_id
        self.parent = parent
        self.report_id = report_id        
        self.publisher = publisher
        self.release_time = release_time
        self.content = content

    def __repr__(self) -> str:
        return f"ReportReply(reply_id={self.reply_id}, parent={self.parent}, report_id={self.report_id}, publisher={self.publisher}, release_time={self.release_time}, content={self.content})"

