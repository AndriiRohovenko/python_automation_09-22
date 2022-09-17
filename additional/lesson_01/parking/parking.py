from typing import List
from car import Car

class Parking:
    def __init__(self, size: int) -> None:
        self.__cars: List[Car] = []
        self.__size = size
        self.__booked = 0
        self.__current = 0

    def __setitem__(self, index: int, car: Car) -> None:
        if self.__booked < self.__size: 
            self.__cars.append(car)
            self.__booked += 1
        else:
            raise Exception(f"Parking max size is {self.__size}")
    
    def __getitem__(self, index: int):
        return self.__cars[index]

    def find(self, year: int) -> int:
        return self.__cars.index(
            list(
                filter(
                    lambda car: car.year == year, 
                    self.__cars
                )
            )[0]
        )

    def __str__(self) -> str:
        car_reprs = []

        for car in self.__cars:
            car_reprs.append(str(car))

        return "\n".join(car_reprs)


    def __iter__(self):
        return self

    def __next__(self) -> Car:
        if self.__current < len(self.__cars):
            car = self.__cars[self.__current]
            self.__current += 1
        else:
            raise StopIteration

        return car
