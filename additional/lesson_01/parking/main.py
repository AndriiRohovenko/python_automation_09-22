from parking import Parking
from car import Car


parking = Parking(5)
parking[0] = (Car("Toyota", 1987, "Yellow"))
parking[1] = (Car("Toyota", 1991, "Yellow"))
parking[2] = (Car("Toyota", 1992, "Yellow"))
parking[3] = (Car("Toyota", 1993, "Yellow"))
parking[4] = (Car("Toyota", 1994, "Yellow"))
# parking[0] = (Car("Toyota", 1995, "Yellow"))

# print(
#     parking[
#         parking.find(1991)
#     ]
# )


# print(parking)


# implicit iterator usage
# for car in parking:
#     print(car)

# explicit iterator usage
parking_iterator = iter(parking)

for car in parking_iterator:
    print(car)
