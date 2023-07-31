from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import transaction
from rest_framework.views import APIView

from .models import VmpayAccount
from .serializers import VmpayAccountSerializer


class AccountView(APIView):
    def get(self, request):
        account = VmpayAccount.objects.all()
        account_serializer = VmpayAccountSerializer(account, many=True)
        return JsonResponse(account_serializer.data, safe=False)

