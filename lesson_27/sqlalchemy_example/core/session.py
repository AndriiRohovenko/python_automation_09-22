from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from lesson_27.sqlalchemy_example.config import config


engine = create_engine(
    f"postgresql://"
    f"{config.db.user}:"
    f"{config.db.password}@"
    f"{config.db.host}/"
    f"{config.db.database}",
    execution_options={
        "isolation_level": "AUTOCOMMIT"
    }
)

session: Session = sessionmaker(engine)()
