from repository.product_repository import IProductRepository
from Model.product import Product
from interfaces import IProductService


class ProductService(IProductService):
    def __init__(self):
        self.setProductRepository()

    def setProductRepository(self):
        self.repository = IProductRepository()

    def processProduct(self, product: Product) -> Product:
        return self.repository.processProduct(product)

    def addProduct(self, product: Product):
        self.repository.addProduct(product)

    def deleteProduct(self, product: Product):
        self.repository.deleteProduct(product)

    def updateProduct(self, product: Product) -> Product:
        return self.repository.updateProduct(product)

    def getProduct(self, product: Product) -> Product:
        return self.repository.getProduct(product)
