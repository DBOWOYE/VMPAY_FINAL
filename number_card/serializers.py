from rest_framework import serializers
from .models import NumberCard

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberCard
        fields = ('get_number', 'is_used')