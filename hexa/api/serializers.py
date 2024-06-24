from rest_framework import serializers
from adapters.database.models import Offer


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'title', 'completed', 'updated', 'user']

