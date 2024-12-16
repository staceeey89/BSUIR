from repository.review_repository import IReviewRepository
from Model.review import Review
from interfaces import IReviewService


class ReviewService(IReviewService):
    def __init__(self):
        self.setReviewRepository()

    def setReviewRepository(self):
        self.repository = IReviewRepository()

    def processReview(self, text: str) -> Review:
        return self.repository.processReview(text)

    def addReview(self, review: Review):
        self.repository.addReview(review)

    def deleteReview(self, review: Review):
        self.repository.deleteReview(review)
