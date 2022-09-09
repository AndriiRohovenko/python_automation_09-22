from __future__ import annotations

from typing import List

from gender import Gender


class User:
    def __init__(
        self, first_name: str, last_name: str, email: str, gender: Gender
    ) -> None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__gender = gender

    @classmethod
    def from_csv(cls, csv_data: str) -> List[User]:
        csv_rows = csv_data.split("\n")
        headers, rows = csv_rows.pop(0), csv_rows
        
        users = []
        
        for row in rows:
            users.append(cls(*(row.split(","))))

        return users

    def to_xml(self) -> str:
        xml_metadata = '<?xml version="1.0" encoding="UTF-8"?>'
        info = ""

        for key, value in self.__dict__.items():
            node_name = self.__get_public_name(key)
            info += f"<{node_name}>{value}</{node_name}>"
        
        data = f"<data>{info}</data>"
        
        return f"{xml_metadata}\n{data}"

    def __get_public_name(self, private_name: str) -> str:
        prefix = f"_{self.__class__.__name__}__"

        if private_name.startswith(prefix):
            return private_name.replace(prefix, "")
        else:
            return private_name

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name