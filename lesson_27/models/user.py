from enum import unique
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import (
    Column,
    String,
)

from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String(32), primary_key=True)
    email = Column(String(128), unique=True)
    profiles = relationship("Profile")