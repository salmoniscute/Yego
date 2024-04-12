from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, BaseType
from models.website_bulletin_file import WebsiteBulletinFile


class WebsiteBulletin(Base):
    __tablename__ = "WebsiteBulletin"
    wb_id : Mapped[BaseType.wb_id]
    title: Mapped[BaseType.str_20]
    release_time: Mapped[BaseType.str_20]
    content: Mapped[BaseType.str_20]
    pin_to_top: Mapped[BaseType.boolean]

    # Relationship to child
    files: Mapped[list["WebsiteBulletinFile"]] = relationship(
        "WebsiteBulletinFile",
        back_populates="website_bulletin_info",
        cascade="all, delete-orphan", 
        passive_deletes=True,
        lazy="joined"
    )

    # Relationship to parent
    publisher: Mapped[str] = mapped_column(ForeignKey("User.uid", ondelete="cascade"))
    publisher_info: Mapped["User"] = relationship(
        "User",
        back_populates="website_bulletins"
    )

    
    def __init__(self, wb_id: str, publisher: str, title: str, release_time: str, content: str, pin_to_top: bool) -> None:
        self.wb_id = wb_id 
        self.publisher = publisher
        self.title = title
        self.release_time = release_time
        self.content = content
        self.pin_to_top = pin_to_top

    def __repr__(self) -> str:
        return f"WebsiteBulletin(wb_id={self.wb_id}, publisher={self.publisher}, title={self.title}, release_time={self.release_time}, content={self.content}, pin_to_top={self.pin_to_top})"
    