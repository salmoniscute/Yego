from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, BaseType


class Notification(Base):
    __tablename__ = "Notification"
    id: Mapped[BaseType.int_id]
    uid: Mapped[BaseType.str_20] = mapped_column(ForeignKey("User.uid", ondelete="CASCADE"))
    component_id: Mapped[BaseType.int_type] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
    have_read: Mapped[BaseType.boolean]
    release_time: Mapped[BaseType.datetime]
    type: Mapped[BaseType.str_20]
    
    # Relationship to parent
    user_info: Mapped["User"] = relationship("User", back_populates="notifications", lazy="joined")
    component_info: Mapped["Component"] = relationship("Component", back_populates="notifications", lazy="joined")

    def __init__(self, uid: str, component_id: str, have_read: bool, release_time: str, type: str) -> None:
        self.uid = uid
        self.component_id = component_id
        self.have_read = have_read
        self.release_time = release_time
        self.type = type
        
    def __repr__(self) -> str:
        return f"Notification(id={self.id}, uid={self.uid}, component_id={self.component_id}, have_read={self.have_read}, release_time={self.release_time}), type={self.type})"
    