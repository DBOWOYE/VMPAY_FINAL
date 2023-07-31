from django.db import models
from customer.models import Customer
from number_card.models import NumberCard
from utils.cryptography import decrypter

class VmpayAccount(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    number_card = models.OneToOneField(NumberCard,on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    accurency = models.CharField(max_length=3, default='GNF')

    
    #Methode de qui nous permet de deposer de l'argent sur le compte
    def deposer(self, montant):
        self.balance +=montant
    
    #Methode de qui nous permet de retirer de l'argent sur le compte
    def retirer(self, montant):
        self.balance -=montant
    
    #Methode qui nous permet de recuperer le solde
    def solde(self):
        return self.balance

class Depot(models.Model):
    pass

class Retrait(models.Model):
    pass

class Transaction(models.Model):
    pass