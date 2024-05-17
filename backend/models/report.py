from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, BaseType


class Report(Base):
    __tablename__ = "Report"
    id: Mapped[BaseType.component_id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))

    # Relationship to parent
    info: Mapped["Component"] = relationship("Component", back_populates="report")

    def __init__(self, id: int) -> None:
        self.id = id

    def __repr__(self) -> str:
        return f"Report(id={self.id})"


class ReportReply(Base):
    __tablename__ = "ReportReply"
    id: Mapped[BaseType.component_id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
    root_id: Mapped[BaseType.int_type] = mapped_column(ForeignKey("Report.id", ondelete="CASCADE"))
    parent_id: Mapped[BaseType.int_type] 

    # Relationship to parent
    info: Mapped["Component"] = relationship("Component", back_populates="reply")

    def __init__(self, id: int, root_id: int, parent_id: int) -> None:
        self.id = id
        self.root_id = root_id
        self.parent_id = parent_id

    def __repr__(self) -> str:
        return f"ReportReply(id={self.id}, root_id={self.root_id}, parent={self.parent_id})"
