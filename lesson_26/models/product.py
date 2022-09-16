from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True)
    name = Column(String(30))
    quontity = Column(Integer)
    price = Column(Integer)

    def __str__(self) -> str:
        return f"{self.id} | {self.name} | {self.quontity} | {self.price}"
