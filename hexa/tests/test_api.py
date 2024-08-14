from rest_framework import status
from .test_setup import TestApiSetup

class TestMyModelLogAPIs(TestApiSetup):
    def test_get_all_my_model(self):
        response = self.client.get('/api/offers')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_my_offer(self):
        response = self.client.get('/api/offers/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
