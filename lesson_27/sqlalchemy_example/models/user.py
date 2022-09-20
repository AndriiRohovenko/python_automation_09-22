from __future__ import annotations

from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    String,
)

from .base import Base
from lesson_27.sqlalchemy_example.core.session import session


class User(Base):
    __tablename__ = "users"

    id = Column(String(32), primary_key=True)
    email = Column(String(128), unique=True)
    profiles = relationship("Profile")

    @classmethod
    def by_email(cls, email: str) -> User:
        return session.query(cls).filter(cls.email == email).one()

    def insert(self) -> None:
        session.add(self)
        session.commit()
