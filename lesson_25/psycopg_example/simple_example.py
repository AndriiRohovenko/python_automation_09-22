from __future__ import annotations

from psycopg2 import connect

from typing import List, Tuple


class Product:
    def __init__(
            self,
            id: str,
            name: str,
            quontity: int,
            price: int,
    ):
        self.__id = id
        self.__name = name
        self.__quontity = quontity
        self.__price = price

    @classmethod
    def from_cursor_data(cls, data: List[Tuple]) -> List[Product]:
        products = []

        for item in data:
            products.append(cls(*item))

        return products

    def __str__(self):
        return f"{self.__name} | {self.__price}"




connection = connect(database="test", user="postgres", password="postgres", host="localhost")

cursor = connection.cursor()

select_all_query = "select * from products;"

update_query = (
    "update products "
    "set price = 1000000 "
    "where id = 'ccccc';"
)

cursor.execute(select_all_query)

result_before_update = cursor.fetchall()

products = Product.from_cursor_data(result_before_update)

for product in products:
    print(product)

cursor.execute(update_query)
connection.commit()

cursor.execute(select_all_query)

result_after_update = cursor.fetchall()

print("-" * 50)
products = Product.from_cursor_data(result_after_update)

for product in products:
    print(product)


