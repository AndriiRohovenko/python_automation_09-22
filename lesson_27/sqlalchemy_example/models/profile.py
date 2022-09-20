from sqlalchemy import (
    Column,
    String,
    ForeignKey,
)

from .base import Base
from lesson_27.sqlalchemy_example.core.session import session


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(String(32), primary_key=True)
    first_name = Column(String(32))
    last_name = Column(String(32))
    country_code = Column(String(3))
    user_id = Column(String(32), ForeignKey("users.id"))

    def insert(self) -> None:
        with session() as s:
            s.add(self)
            s.commit()

    def __str__(self):
        return f"{self.id} | {self.first_name} | {self.last_name} | {self.country_code}"
