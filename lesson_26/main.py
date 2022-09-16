from models.product import Product
from products_registry import ProductsRegistry

registry = ProductsRegistry()


for product in registry.get_all():
    print(product)

# registry.update_price_for(id="aaaaa", price=500)
# registry.delete_one_(id="aaaaa")

print("-" * 50)

# for product in registry.get_all():
#     print(product)

# for product in registry.get_all_with_price_greater_then(price=1000):
#     print(product)

# registry.insert_one(
#     Product(
#         id="opopo",
#         name="Nokia 000",
#         quontity=12,
#         price=25,
#     )
# )
registry.insert_many(
    [
        Product(
            id="jkjkj",
            name="Nokia 001",
            quontity=1,
            price=502,
        ),
        Product(
            id="ioioi",
            name="Nokia 002",
            quontity=2,
            price=505,
        )
    ]
)

for product in registry.get_all():
    print(product)