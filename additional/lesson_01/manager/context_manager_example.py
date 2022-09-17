from __future__ import annotations

from datetime import datetime
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
        self.__write_stream = None

    def __str__(self) -> str:
        return f"{self.__name} | {self.__age} | {self.__gender}"

    def save(self) -> None:
        self.__write_stream.write(str(self))
    
    def __enter__(self) -> Human:
        self.__write_stream = open(f"{datetime.now()}.txt", "w")
        return self
    
    def __exit__(self, *args) -> None:
        if not self.__write_stream.closed:
            self.__write_stream.close()


    # TODO: add examples with super
    # def __getattribute__(self, __name: str) -> Any:
    #     if __name not in super(self.__class__).__dict__:
    #         raise AttributeError(f"{__name} is not exist...")
    #     return self.__dict__[__name]

    # def __getattr__(self, name: str) -> Any:
    #     print(name)