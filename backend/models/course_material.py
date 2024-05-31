from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, BaseType
from datetime import datetime


class CourseMaterial(Base):
    __tablename__ = "CourseMaterial"
    id: Mapped[BaseType.component_id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
    course_id: Mapped[BaseType.int_type] = mapped_column(ForeignKey("Course.id", ondelete="CASCADE"))

    # Relationship to parent
    info: Mapped["Component"] = relationship("Component", back_populates="course_material")
    course_info: Mapped["Course"] = relationship("Course", back_populates="course_materials")

    # Relationship to child
    material_info: Mapped[list["MaterialInfo"]] = relationship(
        "MaterialInfo", 
        back_populates="course_material", 
        cascade="all, delete-orphan",
        lazy="selectin"
    )

    assignment: Mapped[list["Assignment"]] = relationship(
        "Assignment", 
        back_populates="course_material",
        cascade="all, delete-orphan",
        lazy="selectin"
    )

    def __init__(self, id: int, course_id:str) -> None:
        self.id = id
        self.course_id = course_id

    def __repr__(self) -> str:
        return f"CourseMaterial(id={self.id}, course_id={self.course_id})"
    
    
class MaterialInfo(Base):
    __tablename__ = "MaterialInfo"
    id: Mapped[BaseType.component_id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
    material_id: Mapped[BaseType.int_type] = mapped_column(ForeignKey("CourseMaterial.id", ondelete="CASCADE"))
    start_time: Mapped[BaseType.datetime]
    end_time: Mapped[BaseType.datetime]
    display: Mapped[BaseType.boolean]
    
    # Relationship to parent
    info: Mapped["Component"] = relationship("Component", back_populates="material_info")
    course_material: Mapped["CourseMaterial"] = relationship("CourseMaterial", back_populates="material_info")

    def __init__(self, id: int, material_id: int, start_time: datetime, end_time: datetime, display: bool) -> None:
        self.id = id
        self.material_id = material_id
        self.start_time = start_time
        self.end_time = end_time
        self.display = display

    def __repr__(self) -> str:
        return f"MaterialInfo(id={self.id}, material_id={self.material_id}, start_time={self.start_time}, end_time={self.end_time}, display={self.display})"
    

class Assignment(Base):
    __tablename__ = "Assignment"
    id: Mapped[BaseType.component_id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
    material_id: Mapped[BaseType.int_type] = mapped_column(ForeignKey("CourseMaterial.id", ondelete="CASCADE"))
    submitted_type: Mapped[BaseType.str_10]
    submitted_object: Mapped[BaseType.str_10]
    display: Mapped[BaseType.boolean]
    submitted_time: Mapped[BaseType.datetime]
    deadline: Mapped[BaseType.datetime]
    reject_time: Mapped[BaseType.datetime]
    feedback_type: Mapped[BaseType.str_20]
    
    # Relationship to parent
    info: Mapped["Component"] = relationship("Component", back_populates="assignment")
    course_material: Mapped["CourseMaterial"] = relationship("CourseMaterial", back_populates="assignment")

    def __init__(self, id: int, material_id: int, submitted_type: str, submitted_object: str, display: bool, submitted_time: datetime, deadline: datetime, reject_time: datetime, feedback_type: str) -> None:
        self.id = id
        self.material_id = material_id
        self.submitted_type = submitted_type
        self.submitted_object = submitted_object
        self.display = display
        self.submitted_time = submitted_time
        self.deadline = deadline
        self.reject_time = reject_time
        self.feedback_type = feedback_type

    def __repr__(self) -> str:
        return f"Assignment(id={self.id}, material_id={self.material_id}, submitted_type={self.submitted_type}, submitted_object={self.submitted_object}, display={self.display}, submitted_time={self.submitted_time}, deadline={self.deadline}, reject_time={self.reject_time}, feedback_type={self.feedback_type})"
