from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import response
from django.db import transaction
from rest_framework.views import APIView

from number_card.models import NumberCard
from vmp_account.models import VmpayAccount
from .models import Customer
from .serializers import CustomerSerializer

class customerView(APIView):
    def get(self, request, format=None):
        customers = Customer.objects.all()
        customers_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse({'customer':customers_serializer.data}, safe=False)
    
    def post(self, request, format=None):
        customer_data = JSONParser().parse(request)
        customers_serializer = CustomerSerializer(data=customer_data)
        if customers_serializer.is_valid():
            with transaction.atomic():
                customer = customers_serializer.save()
                card = NumberCard.objects.filter(is_used__in=['False']).first()
                if not card is None:
                    VmpayAccount.objects.create(customer = customer, number_card=card)
                    card.is_used = True
                    card.save()
                else:
                    return JsonResponse("Card empty, generate again please !", safe=False)
                return JsonResponse("Customer added successfully !", safe=False)
        return JsonResponse("Failed added customer !", safe=False)
    
class CustomerDetail(APIView):
    def get_object(self, pk):
        try:
          return Customer.objects.select_related('vmpayaccount').get(customer_id=pk)
        except:
          return JsonResponse("Customer not found !", safe=False)
    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return JsonResponse({"Customer": serializer.data})
        
    def put(self, request, pk, format=None):
        customer_data = JSONParser().parser(request)
        customer = self.get_object(pk)
        customers_serializer = CustomerSerializer(customer, data=customer_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse("Customer updated sucessfully", safe=False)
        return JsonResponse("Customer update failed !", safe=False)
    def delete(self, request, pk, format=None):
        customer = self.get_object(pk)
        customer.delete()
        return JsonResponse("Customer deleted successfully !", safe=False)
