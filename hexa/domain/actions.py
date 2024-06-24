from domain.models import DOffer
from domain.database_interface import DatabaseInterface


class GetOffer:
    def __init__(self, database: DatabaseInterface):
        self.__database = database

    def execute(self, offer_id: int) -> DOffer:
        print("-------", self.__database)
        print("offer_id", offer_id)
        return self.__database.get_offer(offer_id)

class GetOffers:
    def __init__(self, database: DatabaseInterface):
        self.__database = database

    def execute(self) -> list[DOffer]:
        return self.__database.get_offers()