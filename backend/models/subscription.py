from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, BaseType


class Subscription(Base):
    __tablename__ = "Subscription"
    id: Mapped[BaseType.subscription_id]
    uid: Mapped[BaseType.str_10] = mapped_column(ForeignKey("User.uid", ondelete="CASCADE"))
    component_id: Mapped[BaseType.int_type] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
    
    # Relationship to parent
    user_info: Mapped["User"] = relationship("User", back_populates="subscriptions")
    component_info: Mapped["Component"] = relationship("Component", back_populates="subscriptions")

    def __init__(self, uid: str, component_id: int) -> None:
        self.uid = uid
        self.component_id = component_id
        
    def __repr__(self) -> str:
        return f"Subscription(id={self.id}, uid={self.uid}, component_id={self.component_id})"
    