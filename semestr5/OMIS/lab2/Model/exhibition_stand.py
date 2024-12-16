from Model.product import Product


class ExhibitionStand:
    def __init__(self, name: str, category: str, product: list[Product]):
        self.name = name
        self.category = category
        self.products = product

    def __str__(self):
        return f"ExhibitionStand {self.name} - {self.category}"
