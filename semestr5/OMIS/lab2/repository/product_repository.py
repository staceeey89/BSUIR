from db_context import DBContext
from Model.product import Product
from interfaces import IProductRepository


class ProductRepository(IProductRepository):
    def __init__(self):
        self.databaseContext = DBContext()

    def processProduct(self, product: Product) -> Product:
        return product  # Simple processing

    def addProduct(self, product: Product):
        # Add to the database
        pass

    def deleteProduct(self, product: Product):
        # Delete from the database
        pass

    def updateProduct(self, product: Product) -> Product:
        return product  # Simple update

    def getProduct(self, product: Product) -> Product:
        return product
