from domain.database_interface import DatabaseInterface
from .models import Offer
from domain.models import DOffer, DUser
import datetime
from django.contrib.auth.models import User


class PostgresAdapter(DatabaseInterface):

    def get_offer(self, offer_id:int, user:User = None) -> DOffer:
        offer = Offer.objects.get(id=offer_id)
        dUser = DUser(offer.user.id,offer.user.email)
        result = DOffer(offer.id, offer.title, offer.completed, datetime.datetime.now(), dUser)
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