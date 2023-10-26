from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta: # Meta Data describing the model while communicating with APIs
        model = Drink
        fields = ["id", "name", "description"]