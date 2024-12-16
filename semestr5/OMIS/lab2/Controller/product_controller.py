from Model.product import Product
from Model.exhibition_stand import ExhibitionStand
from interfaces import IProductController


class ProductController(IProductController):
    def processProduct(self, product: Product) -> Product:
        # Process the product (for example, update details)
        product.name = "Processed " + product.name
        return product

    def addProduct(self, product: Product):
        print(f"Added {product}")

    def deleteProduct(self, product: Product):
        print(f"Deleted {product}")

    def updateProduct(self, product: Product) -> Product:
        product.name = "Updated " + product.name
        return product

    def getProduct(self, product: Product) -> Product:
        return product
