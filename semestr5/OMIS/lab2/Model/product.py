from Model.review import Review
from Model.user import User


class Product:
    def __init__(self, name: str, price: float, product_name: str, representative: User, comm: list[Review]):
        self.name = name
        self.price = price
        self.product_name = product_name
        self.representative = representative
        self.comm = comm

    def __str__(self):
        return f"Product {self.name}, Price {self.price}"
