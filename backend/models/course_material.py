from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, BaseType
from datetime import datetime


class CourseMaterial(Base):
    __tablename__ = "CourseMaterial"
    id: Mapped[BaseType.component_id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
    course_id: Mapped[BaseType.int_type] = mapped_column(ForeignKey("Course.id", ondelete="CASCADE"))

    # Relationship to parent
    info: Mapped["Component"] = relationship("Component", back_populates="course_materials")
    
    course_info: Mapped["Course"] = relationship(
        "Course", 
        back_populates="course_materials",
        lazy="joined"
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
    info: Mapped["Component"] = relationship("Component", back_populates="material_infos")

    def __init__(self, id: int, material_id: int, start_time: datetime, end_time: datetime, display: bool) -> None:
        self.id = id
        self.material_id = material_id
        self.start_time = start_time
        self.end_time = end_time
        self.display = display

    def __repr__(self) -> str:
        return f"MaterialInfo(id={self.id}, material_id={self.material_id}, start_time={self.start_time}, end_time={self.end_time}, display={self.display})"
    

# class SubmittedAssignment(Base):
#     __tablename__ = "SubmittedAssignment"
#     id: Mapped[BaseType.component_id] = mapped_column(ForeignKey("Component.id", ondelete="CASCADE"))
#     assignment_id: Mapped[BaseType.int_type] = mapped_column(ForeignKey("MaterialInfo.id", ondelete="CASCADE"))
#     grade: Mapped[BaseType.int_type]
    
#     # Relationship to parent
#     info: Mapped["Component"] = relationship("Component", back_populates="submitted_assignments")

#     def __init__(self, id: int, assignment_id: int, grade: int) -> None:
#         self.id = id
#         self.assignment_id = assignment_id
#         self.grade = grade

#     def __repr__(self) -> str:
#         return f"SubmittedAssignment(id={self.id}, assignment_id={self.assignment_id}, grade={self.grade})"
