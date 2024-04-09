from typing import Optional 
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey
from models.base import Base, BaseType


class File(Base):
    __tablename__ = "File"
    id: Mapped[BaseType.id]
    component_id: Mapped[BaseType.str_20] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
    path: Mapped[BaseType.str_100]

    # Relationship to parent
    component_info: Mapped["Component"] = relationship(
        "Component",
        back_populates="files"
    )

    def __init__(self, id: str, component_id: str, path: str) -> None:
        self.id = id
        self.component_id = component_id
        self.path = path
        
    def __repr__(self) -> str:
        return f"File(id={self.id}, component_id={self.component_id}), path={self.path}"
