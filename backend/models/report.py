from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, BaseType
from models.component import Component

class Report(Component):
    __tablename__ = "Report"
    id: Mapped[BaseType.id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))

    # Relationship to parent
    info: Mapped["Component"] = relationship(
        "Component",
        back_populates="reports"
    )

    def __init__(self, id: str, uid: str, release_time: str, title: str, content: str) -> None:
        self.id = id
        self.uid = uid
        self.release_time = release_time
        self.title = title
        self.content = content

    def __repr__(self) -> str:
        return f"Report(id={self.id}, uid={self.uid}, release_time={self.release_time}, title={self.title}, content={self.content})"


