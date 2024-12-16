from Model.review import Review
from Model.product import Product
from interfaces import IReviewController


class ReviewController(IReviewController):
    def processReview(self, review: Review) -> Review:
        review.comment = "Processed: " + review.comment
        return review

    def addReview(self, review: Review):
        print(f"Added review: {review}")

    def deleteReview(self, review: Review):
        print(f"Deleted review: {review}")

    def updateReview(self, review: Review) -> Review:
        review.comment = "Updated " + review.comment
        return review

    def getReview(self, review: Review) -> Review:
        return review
