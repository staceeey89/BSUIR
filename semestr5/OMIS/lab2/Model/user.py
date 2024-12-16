from typing import Optional, List
from role import Role


class User:
    def __init__(self, nickname: str, password: Optional[str] = None, role: List[int] = None):
        self.nickname = nickname
        self.password = password
        self.role = role
