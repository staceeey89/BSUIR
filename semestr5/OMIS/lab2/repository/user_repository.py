from db_context import DBContext
from Model.user import User


class UserRepository:
    def __init__(self):
        self.users = {}

    def get_user(self, name: str) -> User:
        return self.users.get(name)

    def create_user(self, user: User) -> bool:
        if user.nickname in self.users:
            return False
        self.users[user.nickname] = user
        return True

    def update_user(self, user: User):
        self.users[user.nickname] = user

    def delete_user(self, name: str):
        self.users.pop(name, None)