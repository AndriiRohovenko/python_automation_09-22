from __future__ import annotations


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

    def __str__(self):
        return f"{self.__name} | {self.__age}"


john = Human.from_dict(
    {
        "name": "John Dow",
        "age": 12
    }
)

print(john)
