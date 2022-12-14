from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from ..config import config


__engine = create_engine(
    f"postgresql://"
    f"{config['db']['user']}:"
    f"{config['db']['password']}@"
    f"{config['db']['host']}/"
    f"{config['db']['database']}",
    execution_options={
        "isolation_level": "AUTOCOMMIT"
    }
)
session = sessionmaker(__engine)

# session: Session = __session()
