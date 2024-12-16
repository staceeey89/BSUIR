from abc import ABC, abstractmethod
from Model.exhibition_stand import ExhibitionStand
from Model.review import Review
from Model.product import Product
from Model.user import User


class IExhibitionStandRepository(ABC):
    @abstractmethod
    def getExhibitionStand(self) -> ExhibitionStand:
        pass

    @abstractmethod
    def getExhibitionStandName(self) -> str:
        pass

    @abstractmethod
    def setExhibitionStandName(self, name: str):
        pass

    @abstractmethod
    def addExhibitionStand(self, stand: ExhibitionStand):
        pass

    @abstractmethod
    def deleteExhibitionStand(self, stand: ExhibitionStand):
        pass


class IExhibitionStandService(ABC):
    @abstractmethod
    def getExhibitionStandName(self) -> str:
        pass

    @abstractmethod
    def setExhibitionStandName(self, name: str):
        pass

    @abstractmethod
    def addExhibitionStand(self, stand: ExhibitionStand):
        pass

    @abstractmethod
    def deleteExhibitionStand(self, stand: ExhibitionStand):
        pass


class IReviewRepository(ABC):
    @abstractmethod
    def processReview(self, text: str) -> Review:
        pass

    @abstractmethod
    def addReview(self, review: Review):
        pass

    @abstractmethod
    def deleteReview(self, review: Review):
        pass


class IReviewService(ABC):
    @abstractmethod
    def processReview(self, text: str) -> Review:
        pass

    @abstractmethod
    def addReview(self, review: Review):
        pass

    @abstractmethod
    def deleteReview(self, review: Review):
        pass


class IProductRepository(ABC):
    @abstractmethod
    def processProduct(self, product: Product) -> Product:
        pass

    @abstractmethod
    def addProduct(self, product: Product):
        pass

    @abstractmethod
    def deleteProduct(self, product: Product):
        pass

    @abstractmethod
    def updateProduct(self, product: Product) -> Product:
        pass

    @abstractmethod
    def getProduct(self, product: Product) -> Product:
        pass


class IProductService(ABC):
    @abstractmethod
    def processProduct(self, product: Product) -> Product:
        pass

    @abstractmethod
    def addProduct(self, product: Product):
        pass

    @abstractmethod
    def deleteProduct(self, product: Product):
        pass

    @abstractmethod
    def updateProduct(self, product: Product) -> Product:
        pass

    @abstractmethod
    def getProduct(self, product: Product) -> Product:
        pass


class IUserRepository(ABC):
    @abstractmethod
    def getUser(self, name: str) -> User:
        pass

    @abstractmethod
    def createUser(self, user: User):
        pass

    @abstractmethod
    def updateUser(self, user: User):
        pass

    @abstractmethod
    def deleteUser(self, name: str):
        pass


class IUserService(ABC):
    @abstractmethod
    def register(self, user: User) -> bool:
        pass

    @abstractmethod
    def login(self, name: str, password: str) -> bool:
        pass

    @abstractmethod
    def updateUser(self, user: User):
        pass

    @abstractmethod
    def deleteUser(self, name: str):
        pass
