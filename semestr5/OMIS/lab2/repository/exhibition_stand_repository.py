from db_context import DBContext
from Model.exhibition_stand import ExhibitionStand
from interfaces import IExhibitionStandRepository


class ExhibitionStandRepository(IExhibitionStandRepository):
    def __init__(self):
        self.databaseContext = DBContext()

    def getExhibitionStand(self) -> ExhibitionStand:
        # Fetch from database
        return ExhibitionStand(name="Example Stand", products=[])

    def getExhibitionStandName(self) -> str:
        return "Exhibition Stand Name"

    def setExhibitionStandName(self, name: str):
        # Update name in the database
        pass

    def addExhibitionStand(self, stand: ExhibitionStand):
        # Add to the database
        pass

    def deleteExhibitionStand(self, stand: ExhibitionStand):
        # Delete from the database
        pass
