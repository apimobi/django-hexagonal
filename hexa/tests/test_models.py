from django.test import TestCase
from adapters.database.models import Offer


class OfferTest(TestCase):
    """ Test module for Offer model """

    def setUp(self):
        Offer.objects.create(
            title='test model 1', completed=False)
        Offer.objects.create(
            title='test model 2', completed=True)

    def test_offer_breed(self):
        offer1 = Offer.objects.get(title='test model 1')
        offer2 = Offer.objects.get(title='test model 2')
        self.assertEqual(
            offer1.completed, False)
        self.assertEqual(
            offer2.completed, True)