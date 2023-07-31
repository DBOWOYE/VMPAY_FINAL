from rest_framework import serializers

from customer.models import Customer
from vmp_account.models import VmpayAccount
from vmp_account.serializers import VmpayAccountSerializer



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'first_name', 'last_name', 'phone', 'country', 'town', 'is_active']
