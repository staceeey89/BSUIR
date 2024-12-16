from repository.exhibition_stand_repository import IExhibitionStandRepository
from Model.exhibition_stand import ExhibitionStand
from interfaces import IExhibitionStandService


class ExhibitionStandService(IExhibitionStandService):
    def __init__(self):
        self.setExhibitionStandRepository()

    def setExhibitionStandRepository(self):
        self.repository = IExhibitionStandRepository()

    def getExhibitionStand(self) -> ExhibitionStand:
        return self.repository.getExhibitionStand()

    def getExhibitionStandName(self) -> str:
        return self.repository.getExhibitionStandName()

    def setExhibitionStandName(self, name: str):
        self.repository.setExhibitionStandName(name)

    def addExhibitionStand(self, stand: ExhibitionStand):
        self.repository.addExhibitionStand(stand)

    def deleteExhibitionStand(self, stand: ExhibitionStand):
        self.repository.deleteExhibitionStand(stand)
