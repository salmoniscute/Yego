from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from models.base import Base, BaseType


class Bulletin(Base):
    __tablename__ = "Bulletin"
    id: Mapped[BaseType.component_id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
    type: Mapped[BaseType.str_20]
    pin_to_top: Mapped[BaseType.boolean]

    __mapper_args__ = {
        "polymorphic_identity": "bulletin",
        "polymorphic_on": "type"
    }
    

class WebsiteBulletin(Bulletin):
    # Relationship to parent
    info: Mapped["Component"] = relationship("Component", back_populates="website_bulletin")

    __mapper_args__ = {
        "polymorphic_identity": "website_bulletin",
    }

    def __init__(self, id: int, pin_to_top: bool) -> None:
        self.id = id
        self.pin_to_top = pin_to_top
        
    def __repr__(self) -> str:
        return f"WebsiteBulletin(id={self.id}, pin_to_top={self.pin_to_top})"


class CourseBulletin(Bulletin):
    course_id: Mapped[BaseType.int_type] = mapped_column(ForeignKey("Course.id", ondelete="CASCADE"), nullable=True)

    # Relationship to parent
    info: Mapped["Component"] = relationship("Component", back_populates="course_bulletin")
    course_info: Mapped["Course"] = relationship("Course", back_populates="course_bulletins", lazy="joined")

    __mapper_args__ = {
        "polymorphic_identity": "course_bulletin",
    }

    def __init__(self, id: int, course_id: str, pin_to_top: bool) -> None:
        self.id = id
        self.course_id = course_id 
        self.pin_to_top = pin_to_top
        
    def __repr__(self) -> str:
        return f"CourseBulletin(id={self.id}, course_id={self.course_id}, pin_to_top={self.pin_to_top})"
