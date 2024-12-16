from user_controller import UserController
from exhibition_stand_controller import ExhibitionStandController
from product_controller import ProductController
from review_controller import ReviewController


class MainController:
    def __init__(self):
        self.initControllers = [
            UserController(),
            ExhibitionStandController(),
            ProductController(),
            ReviewController()
        ]
