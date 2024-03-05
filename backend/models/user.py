import hashlib
from sqlalchemy.orm import Mapped, relationship
from typing import Optional 

from models.base import Base, BaseType


class User(Base):
    __tablename__ = "User"
    uid: Mapped[BaseType.uid]
    password: Mapped[BaseType.hashed_password]
    name: Mapped[BaseType.str_20]
    role: Mapped[BaseType.str_20]
    email: Mapped[BaseType.str_50]
    department: Mapped[BaseType.str_20]
    country: Mapped[BaseType.str_20]
    introduction: Mapped[BaseType.optional_str_200]
    avatar: Mapped[BaseType.optional_str_200]

    def __init__(self, uid: str, password: str, name: str, role: str, email: str, department: str, country: str, introduction: Optional[str], avatar: Optional[str]) -> None:
        self.uid = uid
        self.password = password
        self.name = name
        self.role = role
        self.email = email
        self.department = department
        self.country = country
        self.introduction = introduction
        self.avatar = avatar

    def __repr__(self) -> str:
        return f"User(uid={self.uid}, password={self.password}, name={self.name}, role={self.role}, email={self.email}, department={self.department}, country={self.country}, introduction={self.introduction}, avatat={self.avatar})"
    