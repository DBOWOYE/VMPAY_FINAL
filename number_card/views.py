from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from random import randint
from utils.cryptography import crypter

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


from .models import NumberCard
from .serializers import CardSerializer

def generate_number(request):
    generated_numbers = set()
    while len(generated_numbers) < 10:
        number = str(randint(100000000, 999999999))
        #Créer une fonction de cryptage à part y compris le decryptage
        encrypt_number = crypter(number)
        if not NumberCard.objects.filter(card_number=encrypt_number).exists():
            generated_numbers.add(encrypt_number)
            NumberCard.objects.create(card_number=encrypt_number)

    return HttpResponse("succès !")

def get_card_number(request, *args, **kwargs):
    #cards = Card.objects.filter(is_used__in=[False]).values()
    cards = NumberCard.objects.order_by("-id")
    cards_serializer = CardSerializer(cards, many=True)
    return JsonResponse(cards_serializer.data, safe=False)


