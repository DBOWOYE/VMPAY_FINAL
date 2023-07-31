
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from number_card.models import NumberCard
import random
from utils.cryptography import crypter

from twilio.rest import Client
import random
from Vmpay.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER
from number_card.serializers import CardSerializer


@api_view(['POST'])
def login(request):
    card = request.data
    print(request.data['card_number'])
    
    return JsonResponse(card, safe=False)
    # card_data = JSONParser().parse(request)
    # print(card_data)
    # # card_crypt = crypter(card_data['number'])
    # card_crypt = crypter('794761536')
    # card = NumberCard.objects.get(card_number=card_crypt).values()
    # print(card)
    # if not card is None:
    #     return JsonResponse("Success", safe=False)
    # else:
    #     return JsonResponse("Card not exist !", safe=False)
    
    
    
class VerificationApi(APIView):
    def post(self, request):
        verification_data = JSONParser().parse(request)
        phone_number = verification_data['phone_number']
        print(phone_number)
        verification_code = str(random.randint(100000, 999999))
        
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        message = client.messages.create(
            body=f"Votre code d'activation est : {verification_code}",
            from_=TWILIO_PHONE_NUMBER,
            to= phone_number
        )
        return JsonResponse("success !", safe=False)