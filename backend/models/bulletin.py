from typing import Optional 
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey

from models.base import Base, BaseType
from models.component import Component


class Bulletin(Component):
    __tablename__ = "Bulletin"
    id: Mapped[BaseType.id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
    type: Mapped[BaseType.str_100]
    pin_to_top: Mapped[BaseType.boolean]

    __mapper_args__ = {
        "polymorphic_identity": "bulletin",
        "polymorphic_on": "type"
    }

    # Relationship to parent
    info: Mapped["Component"] = relationship(
        "Component",
        back_populates="bulletins",
        lazy="joined"
    )
    
    def __init__(self, id: str, course_id: str, pin_to_top: bool, type: str) -> None:
        self.id = id
        self.course_id = course_id 
        self.type = type
        self.pin_to_top = pin_to_top
        
    def __repr__(self) -> str:
        return f"Bulletin(id={self.id}, course_id={self.course_id}, type={self.type}),  pin_to_top={self.pin_to_top}"


class WebsiteBulletin(Bulletin):
    __mapper_args__ = {
        "polymorphic_identity": "website_bulletin",
    }

class CourseBulletin(Bulletin):
    course_id: Mapped[BaseType.str_20] = mapped_column(ForeignKey("Course.id", ondelete="CASCADE", nullable=True))
    
    # Relationship to parent
    course_info: Mapped["Course"] = relationship(
        "Course",
        back_populates="bulletins",
        lazy="joined"
    )
                                                
    __mapper_args__ = {
        "polymorphic_identity": "course_bulletin",
    }
