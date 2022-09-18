from __future__ import annotations

from typing import Any


class Human:
    def __init__(
        self,
        name: str,
        age: int,
        gender: str,
    ) -> None:
        self.__name = name
        self.__age = age
        self.__gender = gender

    @classmethod
    def __make(cls) -> Human:
        return cls("John Dow", 31, "Male")

    def __add__(self, other: Human) -> Human:
        return self.__class__.__make()

    def __radd__(self, other: Any) -> Human:
        return self.__class__("Marta Dow", 32, "Female")

    def __iadd__(self, other: int) -> None:
        self.__age += other

        return self
        
    @property
    def name(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return f"{self.__name} | {self.__age} | {self.__gender}"
