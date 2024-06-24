from domain.database_interface import DatabaseInterface
from .models import Offer
from domain.models import DOffer
import datetime


class PostgresAdapter(DatabaseInterface):

    def get_offer(self, offer_id: int) -> DOffer:
        print("offer_id", offer_id)
        offer = Offer.objects.get(id=offer_id)
        dUser = {
            "id": offer.user.id,
            "username": offer.user.username,
            "email": offer.user.email
        }
        print('>>>>', dUser)
        result = DOffer(offer.id, offer.title, offer.completed, datetime.datetime.now())
        return result

    def get_offers(self) -> list[DOffer]:
        offers = Offer.objects.all()
        results = []
        for offer in offers:
            result = DOffer(offer.id, offer.title, offer.completed, datetime.datetime.now())
            results.append(result)
        return results

    def count_offers(self) -> int:
        count = Offer.objects.count()
        return count