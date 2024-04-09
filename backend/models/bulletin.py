from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey

from models.base import BaseType
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
    

class WebsiteBulletin(Bulletin):
    # Relationship to parent
    info: Mapped["Component"] = relationship(
        "Component",
        back_populates="website_bulletins",
        lazy="joined"
    )

    __mapper_args__ = {
        "polymorphic_identity": "website_bulletin",
    }

    def __init__(self, id: str, uid: str, release_time: str, title: str, content: str, pin_to_top: bool) -> None:
        self.id = id
        self.uid = uid
        self.release_time = release_time
        self.title = title
        self.content = content
        self.pin_to_top = pin_to_top
        
    def __repr__(self) -> str:
        return f"WebsiteBulletin(id={self.id}, uid={self.uid}, release_time={self.release_time}, title={self.title}, content={self.content}, pin_to_top={self.pin_to_top}"


class CourseBulletin(Bulletin):
    course_id: Mapped[BaseType.str_20] = mapped_column(ForeignKey("Course.id", ondelete="CASCADE"), nullable=True)

    # Relationship to parent
    info: Mapped["Component"] = relationship(
        "Component",
        back_populates="course_bulletins",
        lazy="joined"
    )

    course_info: Mapped["Course"] = relationship(
        "Course",
        back_populates="course_bulletins"
    )

    __mapper_args__ = {
        "polymorphic_identity": "course_bulletin",
    }

    def __init__(self, id: str, uid: str, release_time: str, title: str, content: str, course_id: str, pin_to_top: bool) -> None:
        self.id = id
        self.uid = uid
        self.release_time = release_time
        self.title = title
        self.content = content
        self.course_id = course_id 
        self.pin_to_top = pin_to_top
        
    def __repr__(self) -> str:
        return f"CourseBulletin(id={self.id}, uid={self.uid}, release_time={self.release_time}, title={self.title}, content={self.content}, course_id={self.course_id}, pin_to_top={self.pin_to_top}"
