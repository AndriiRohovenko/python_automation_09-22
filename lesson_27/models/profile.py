from enum import unique
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)

from .base import Base


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(String(32), primary_key=True)
    first_name = Column(String(32))
    last_name = Column(String(32))
    country_code = Column(String(3))
    user_id = Column(String(32), ForeignKey("users.id"))