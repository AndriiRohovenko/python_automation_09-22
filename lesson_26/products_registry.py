from itertools import product
from sre_constants import LITERAL_UNI_IGNORE
from typing import List

from models.product import Product


class ProductsRegistry:
    def __init__(self) -> None:
        from core.session import session

        self.__session = session

    def get_all(self) -> List[Product]:
        with self.__session() as session:
            products = session.query(Product).order_by(Product.price).all()

        return products

    def get_all_with_price_greater_then(self, price: int) -> List[Product]:
        with self.__session() as session:
            products = session.query(Product).filter(Product.price > price).all()

        return products

    def update_price_for(self, id: str, price: int) -> None:
        with self.__session() as session:
            session.query(Product).filter(Product.id==id).update({Product.price: price})

    def delete_one_(self, id: str) -> None:
        with self.__session() as session:
            session.query(Product).filter(Product.id==id).delete()

    def insert_one(self, product: Product) -> None:
        with self.__session() as session:
            session.add(product)
            session.commit()

    def insert_many(self, products: List[Product]) -> None:
        with self.__session() as session:
            session.add_all(products)
            session.commit()
    