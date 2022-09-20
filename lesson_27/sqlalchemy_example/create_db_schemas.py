from lesson_27.sqlalchemy_example.core import engine
from lesson_27.sqlalchemy_example.models import Base


Base.metadata.create_all(engine)
