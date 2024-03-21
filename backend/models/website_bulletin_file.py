from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, BaseType


class WebsiteBulletinFile(Base):
    __tablename__ = "WebsiteBulletinFile"
    file_id : Mapped[BaseType.wb_file_id]
    path : Mapped[BaseType.str_100]

    # Relationship to parent 
    wb_id: Mapped[str] = mapped_column(ForeignKey("WebsiteBulletin.wb_id", ondelete="cascade"))
    website_bulletin_info: Mapped["WebsiteBulletin"] = relationship(
        "WebsiteBulletin",
        back_populates="files"
    )

    def __init__(self, file_id: str, wb_id: str, path: str) -> None:
        self.file_id = file_id
        self.wb_id = wb_id 
        self.path = path

    def __repr__(self) -> str:
        return f"WebsiteBulletinFile(file_id={self.file_id}, wb_id={self.wb_id}, path={self.path})"
    