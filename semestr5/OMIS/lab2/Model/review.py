from Model.user import User


class Review:
    def __init__(self, text: str, author: User,  comment: str, rating: int):
        self.text = text
        self.author = author
        self.comment = comment
        self.rating = rating

    def __str__(self):
        return f"Review: {self.comment}, Rating: {self.rating}"
