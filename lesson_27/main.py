from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from config import config
from models import Base


engine = create_engine(
    f"postgresql://"
    f"{config['db']['user']}:"
    f"{config['db']['password']}@"
    f"{config['db']['host']}/"
    f"{config['db']['database']}",
    execution_options={
        "isolation_level": "AUTOCOMMIT"
    }
)


Base.metadata.create_all(engine)

session = sessionmaker(engine)
