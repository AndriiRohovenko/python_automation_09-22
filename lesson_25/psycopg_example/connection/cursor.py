from typing import List, Tuple


class Cursor:
    def __init__(self, connection) -> None:
        self.__virtual_data = connection.cursor()

    def fetch_all(self) -> List[Tuple]:
        return self.__virtual_data.fetchall()

    def execute(self, query: str):
        self.__virtual_data.execute(query)