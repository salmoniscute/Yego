from sqlalchemy.orm import Mapped, relationship

from models.base import Base, BaseType


class WebsiteBulletinFile(Base):
    __tablename__ = "WebsiteBulletinFile"
    file_id : Mapped[BaseType.wb_file_id]
    wb_id : Mapped[BaseType.wb_id]
    path : Mapped[BaseType.str_100]

    def __init__(self, file_id: str, wb_id: str, path: str) -> None:
        self.file_id = file_id
        self.wb_id = wb_id 
        self.path = path

    def __repr__(self) -> str:
        return f"WebsiteBulletinFile(file_id={self.file_id}, wb_id={self.wb_id}, path={self.path})"
    