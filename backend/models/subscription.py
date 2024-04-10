from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, BaseType


class Subscription(Base):
    __tablename__ = "Subscription"
    uid: Mapped[BaseType.id] = mapped_column(ForeignKey("User.uid", ondelete="CASCADE"))
    component_id: Mapped[BaseType.id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
    
    # Relationship to parent
    user_info: Mapped["User"] = relationship(
        "User",
        back_populates="subscriptions"
    )

    component_info: Mapped["Component"] = relationship(
        "Component",
        back_populates="subscriptions",
    )

    def __init__(self, uid: str, component_id: str) -> None:
        self.uid = uid
        self.component_id = component_id
        
    def __repr__(self) -> str:
        return f"Subscription(uid={self.uid}, component_id={self.component_id})"
    