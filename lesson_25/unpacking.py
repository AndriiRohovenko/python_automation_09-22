from __future__ import annotations


john = {
    "name": "John Dow",
    "age": 12
}


class Human:
    def __init__(
        self,
        name: str,
        age: int,
    ):
        self.__name = name
        self.__age = age

    @classmethod
    def from_dict(cls, data: dict) -> Human:
        return cls(**data)

