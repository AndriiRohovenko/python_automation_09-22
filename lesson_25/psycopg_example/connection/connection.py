from psycopg2 import connect

from .config import config
from .cursor import Cursor


class Connection:
    def __init__(self) -> None:
        self.__connection = connect(**config['db'])
        self.__cursor = Cursor(self.__connection)

    @property
    def cursor(self) -> Cursor:
        return self.__cursor

    def commit(self):
        self.__connection.commit()