from abc import ABC, abstractmethod
from domain.models import DOffer
from django.contrib.auth.models import User


class DatabaseInterface(ABC):
    @abstractmethod
    def get_offer(self, offer_id:int, user:User=None) -> DOffer:
        pass    
    
    @abstractmethod
    def get_offers(self) -> list[DOffer]:
        pass

    @abstractmethod
    def count_offers(self) -> int:
        pass