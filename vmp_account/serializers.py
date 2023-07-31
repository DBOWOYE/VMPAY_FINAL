from rest_framework import serializers
from .models import VmpayAccount


class VmpayAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = VmpayAccount
        fields = ['number_card','customer', 'balance', 'accurency']