from domain.models import DOffer
from domain.database_interface import DatabaseInterface
from django.contrib.auth.models import User


class GetOffer:
    def __init__(self, database: DatabaseInterface):
        self.__database = database

    def execute(self, offer_id: int, user:User=None) -> DOffer:
        return self.__database.get_offer(offer_id, user)

class GetOffers:
    def __init__(self, database: DatabaseInterface):
        self.__database = database

    def execute(self) -> list[DOffer]:
        return self.__database.get_offers()