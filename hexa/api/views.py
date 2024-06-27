from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from domain.models import DOffer
from .serializers import DOfferSerializer, OfferSerializer
from domain.actions import GetOffer
from adapters.database.adapter import PostgresAdapter
from adapters.database.models import Offer
import json
from .renderer import AlreadyJSONRenderer

class OfferDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [IsAuthenticatedOrReadOnly]
    getOffer = GetOffer(PostgresAdapter())
    # renderer_classes = [AlreadyJSONRenderer]

    # 3. Retrieve
    def get(self, request, offer_id, *args, **kwargs):
        '''
        Retrieves the Offer with given offer_id
        '''

        print(request.user)
        offer_instance = self.getOffer.execute(offer_id, request.user)
        # offer_instance = Offer.objects.get(id=offer_id)
        if not offer_instance:
            return Response(
                {"res": "Object with offer id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = DOfferSerializer(offer_instance)
        return Response(data.data, status=status.HTTP_200_OK)


class OfferListApiView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the offer items
        '''
        offers = Offer.objects.all()
        serializer = OfferSerializer(offers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 1. List all mine
    def getMyOffers(self, request, *args, **kwargs):
        '''
        List all the offer items for given requested user
        '''
        offers = Offer.objects.filter(user = request.user.id)
        serializer = OfferSerializer(offers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        print(request.user)
        '''
        Create the Offer with given offer data
        '''
        data = {
            'title': request.data.get('title'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = OfferSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)