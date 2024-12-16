from Model.user import User
from interfaces import IUserController


class UserController(IUserController):
    def handleLogin(self, num: str, password: str) -> User:
        if self.validateLogin(num, password):
            return User(num)
        raise ValueError("Invalid credentials")

    def handleRegistration(self, num: str, password: str) -> User:
        if self.validateRegistretion(num, password):
            return User(num)
        raise ValueError("Registration failed")

    def showProfile(self, user: User):
        # Display user profile
        print(f"User Profile: {user}")

    def handleUpdateUser(self, user: User):
        # Update user profile
        print(f"Updated {user}")

    def handleDeleteUser(self, user: User):
        # Delete user profile
        print(f"Deleted {user}")

    def validateLogin(self, num: str, password: str) -> bool:
        return num == "123" and password == "password"  # Simple validation

    def validateRegistretion(self, num: str, password: str) -> bool:
        return len(password) > 5  # Simple validation
