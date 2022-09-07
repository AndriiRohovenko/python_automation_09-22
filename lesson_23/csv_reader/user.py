from __future__ import annotations

from typing import Dict, List
from .gender import Gender


class User:
    def __init__(
        self, first_name: str, last_name: str, email: str, gender: Gender
    ) -> None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__gender = gender

    @classmethod
    def from_csv(cls, csv_data: Dict[str, List[str]]) -> List[User]:
        ...
        # Mast have
        # TODO: add implementation to parce data from csv data dict and set all fields

    # TODO: implement __add__ method
    # TODO: implement __sub__ method
    # TODO: implement __str__ method:
    # {
    #     "first_name": "John",
    #     "last_name": "Dow",
    #     "email": "john.dow@gmail.com",
    #     "gender": "MALE"
    # }
