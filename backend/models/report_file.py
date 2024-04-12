from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from models.base import Base, BaseType

class ReportFile(Base):
    __tablename__ = "ReportFile"
    file_id : Mapped[BaseType.file_id]
    report_id : Mapped[BaseType.str_20]
    path : Mapped[BaseType.str_100]

    # relationship to Report child to parent
    report_id : Mapped[BaseType.str_20] = mapped_column(ForeignKey("Report.report_id", ondelete="CASCADE"))
    report : Mapped["Report"] = relationship(
        "Report", 
        back_populates="files"
    )
    
    def __init__(self,file_id:str, report_id:str, path:str) -> None:
        self.file_id = file_id
        self.report_id = report_id
        self.path = path

    def __repr__(self) -> str:
        return f"ReportFile(file_id={self.file_id}, report_id={self.report_id}, path={self.path})"

