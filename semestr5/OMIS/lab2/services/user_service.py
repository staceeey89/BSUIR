from Model.user import User
from repository.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def register_user(self, nickname: str, password: str, roles: list[str]) -> bool:
        user = User(nickname=nickname, password=password, roles=roles)
        return self.repository.create_user(user)

    def authenticate_user(self, nickname: str, password: str) -> bool:
        user = self.repository.get_user(nickname)
        return user and user.password == password