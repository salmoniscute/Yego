from typing import Optional 
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from models.base import Base, BaseType

class Report(Base):
    __tablename__ = "Report"
    report_id : Mapped[BaseType.report_id]
    publisher : Mapped[BaseType.str_20]
    title : Mapped[BaseType.str_100]
    release_time : Mapped[BaseType.str_20]
    content : Mapped[BaseType.str_100]

    # relationship to ReportFile parent to child
    files : Mapped[list["ReportFile"]] = relationship(
        "ReportFile",
        back_populates="report",
        cascade="all, delete, delete-orphan",
        passive_deletes=True,
        lazy="joined"
    )
    
    # relationship to report_reply parent to child
    replies : Mapped[list["ReportReply"]] = relationship(
        "ReportReply",
        back_populates="report",
        cascade="all, delete, delete-orphan",
        passive_deletes=True,
        lazy="joined"
    )
    
    # relationship to User child to parent
    publisher : Mapped[BaseType.str_20] = mapped_column(ForeignKey("User.uid", ondelete="CASCADE"))
    publisher_info : Mapped["User"] = relationship(
        "User", 
        back_populates="reports"
    )
    
    def __init__(self, report_id:str, publisher:str, title:str, release_time:str, content:str) -> None:
        self.report_id = report_id
        self.publisher = publisher
        self.title = title
        self.release_time = release_time
        self.content = content

    def __repr__(self) -> str:
        return f"Report(report_id={self.report_id}, publisher={self.publisher}, title={self.title}, release_time={self.release_time}, content={self.content})"

