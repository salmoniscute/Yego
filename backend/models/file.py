from typing import Optional 
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey
from models.base import Base, BaseType


class File(Base):
    __tablename__ = "File"
    id: Mapped[BaseType.id]
    owner: Mapped[BaseType.id] = mapped_column(ForeignKey("User.uid", ondelete="CASCADE"))
    component_id: Mapped[BaseType.id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
    path: Mapped[BaseType.str_100]

    # Relationship to parent
    owner_info: Mapped["User"] = relationship(
        "User",
        back_populates="files",
        lazy="joined"
    )

    component_info: Mapped["Component"] = relationship(
        "Component",
        back_populates="files",
        lazy="joined"
    )


    def __init__(self, id: str, owner: str, component_id: str, path: str) -> None:
        self.id = id
        self.owner = owner
        self.component_id = component_id
        self.path = path
        
    def __repr__(self) -> str:
        return f"File(id={self.id}, owner={self.owner}, component_id={self.component_id}), path={self.path}"
