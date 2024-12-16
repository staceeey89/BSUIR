from db_context import DBContext
from Model.review import Review
from interfaces import IReviewRepository


class ReviewRepository(IReviewRepository):
    def __init__(self):
        self.databaseContext = DBContext()

    def processReview(self, text: str) -> Review:
        return Review(text=text, author=None)

    def addReview(self, review: Review):
        # Add to the database
        pass

    def deleteReview(self, review: Review):
        # Delete from the database
        pass
