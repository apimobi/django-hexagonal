import uuid
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from adapters.database.models import Offer

class TestApiSetup(TestCase):

    def setUp(self):
        self.client = APIClient()
        fake_email = f"{str(uuid.uuid4())}@email.com"
        self.user = User.objects.create(
            email=str(uuid.uuid4()),
        )
        self.offer = Offer.objects.create(
            title = 'test model 0',
            completed = False,
            user = self.user
        )