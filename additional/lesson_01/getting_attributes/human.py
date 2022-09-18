"""
    1. If you will implement __getattribute__ you should use super to escape
    infinite loop.
    2. If you will implement getattr and getattribute: 
        * getattribute will handle the call and then if no attribute will be 
        detected in instance program thread will be redirected to getattr. 
"""

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

    def __getattr__(self, key: str):
        """
            This method will be called 
            if python will not find attribute on instance of class.
        """
        return None

    def __getattribute__(self, __name: str) -> Any:
        """
            This method will handle all attempts to get attribute 
            from class before __getattr__.
        """

        return super().__getattribute__(__name)

    @property
    def age(self) -> int:
        return self.__age
