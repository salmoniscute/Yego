from typing import Optional 
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey
from models.base import Base, BaseType


class CourseBulletinFile(Base):
    __tablename__ = "CourseBulletinFile"
    file_id : Mapped[BaseType.file_id]
    path : Mapped[BaseType.str_100]
    
    #relationship to parent
    cb_id : Mapped[BaseType.str_20] = mapped_column(ForeignKey("CourseBulletin.cb_id", ondelete="CASCADE"))
    course_bulletin : Mapped["CourseBulletin"] = relationship(
        "CourseBulletin", 
        back_populates="files"
    )


    def __init__(self, file_id:str, path:str, cb_id:str) -> None:
        self.file_id = file_id
        self.path = path
        self.cb_id = cb_id
        

    def __repr__(self) -> str:
        return f"Course bulletin file(file_id={self.file_id}, path={self.path})"

