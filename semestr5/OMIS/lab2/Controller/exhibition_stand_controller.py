from Model.exhibition_stand import ExhibitionStand
from interfaces import IExhibitionStandController


class ExhibitionStandController(IExhibitionStandController):
    def getStandName(self, stand: ExhibitionStand) -> str:
        return stand.name

    def getStandCategory(self, stand: ExhibitionStand) -> str:
        return stand.category

    def updateStand(self, stand: ExhibitionStand) -> ExhibitionStand:
        stand.name = "Updated Stand"
        return stand
