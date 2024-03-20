from sqlalchemy.orm import Mapped

from models.base import Base, BaseType


class WebsiteBulletin(Base):
    __tablename__ = "WebsiteBulletin"
    wb_id : Mapped[BaseType.wb_id]
    publisher: Mapped[BaseType.str_20]
    title: Mapped[BaseType.str_20]
    release_time: Mapped[BaseType.str_20]
    content: Mapped[BaseType.str_20]
    pin_to_top: Mapped[BaseType.boolean]

    def __init__(self, wb_id: str, publisher: str, title: str, release_time: str, content: str, pin_to_top: bool) -> None:
        self.wb_id = wb_id 
        self.publisher = publisher
        self.title = title
        self.release_time = release_time
        self.content = content
        self.pin_to_top = pin_to_top

    def __repr__(self) -> str:
        return f"WebsiteBulletin(wb_id={self.wb_id}, publisher={self.publisher}, title={self.title}, release_time={self.release_time}, content={self.content}, pin_to_top={self.pin_to_top})"
    