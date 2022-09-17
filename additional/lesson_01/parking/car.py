class Car:
    def __init__(
        self,
        model: str,
        year: int,
        color: str
    ) -> None:
        self.__model = model
        self.__year = year
        self.__color = color

    def __str__(self) -> str:
        return f"{self.__model} | {self.__year} | {self.__color}"

    @property
    def year(self) -> int:
        return self.__year
