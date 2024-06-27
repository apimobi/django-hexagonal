from rest_framework import serializers
from adapters.database.models import Offer
import json

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ["id", "title", "completed", "updated", "user"]

class DUserSerializer(serializers.Serializer):
    id= serializers.IntegerField()
    email = serializers.EmailField()

class DOfferSerializer(serializers.Serializer):
    id= serializers.IntegerField()
    completed = serializers.BooleanField()
    updated = serializers.DateTimeField()
    user = DUserSerializer()