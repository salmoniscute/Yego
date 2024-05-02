from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import BaseType
from models.component import Component


class Report(Component):
    __tablename__ = "Report"
    id: Mapped[BaseType.int_id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))

    # Relationship to parent
    info: Mapped["Component"] = relationship("Component", back_populates="report")


    def __init__(self, uid: str, release_time: str, title: str, content: str) -> None:
        self.uid = uid
        self.release_time = release_time
        self.title = title
        self.content = content

    def __repr__(self) -> str:
        return f"Report(uid={self.uid}, release_time={self.release_time}, title={self.title}, content={self.content})"
    
class ReportReply(Component):
    __tablename__ = "ReportReply"
    id: Mapped[BaseType.int_id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
    root_id: Mapped[BaseType.int_type] = mapped_column(ForeignKey("Report.id", ondelete="CASCADE"))
    parent_id: Mapped[BaseType.int_type] 

    # Relationship to parent
    # report_info: Mapped["Report"] = relationship(
    #     "Report",
    #     back_populates="replies"
    # )

    def __init__(self, uid: str, root_id: int, parent_id: int, release_time: str, title: str, content: str) -> None:
        self.uid = uid
        self.root_id = root_id
        self.parent_id = parent_id
        self.release_time = release_time
        self.title = title
        self.content = content

    def __repr__(self) -> str:
        return f"ReportReply(uid={self.uid}, root_id={self.root_id}, parent={self.parent_id}, release_time={self.release_time}, title={self.title}, content={self.content})"
