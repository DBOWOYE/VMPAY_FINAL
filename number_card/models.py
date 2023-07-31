from cryptography.fernet import Fernet
from django.db import models
from djongo import models as djongo_models
#Importation de Fernet pour crypter les données
from utils.cryptography import decrypter

class NumberCard(models.Model):
    #Création du modele Card
    card_number = models.CharField(max_length=255, unique=True)
    is_used = models.BooleanField(default=False)
    

    # Redefinition de la methode save pour crypter le champ card_number lors de l'enregistrement
    """def save(self, *args, **kwargs):
        #Chiffrement du numéro avant de le sauvegarder
        self.card_number = cypher.encrypt(self.card_number.encode()).decode()
        super().save(*args, **kwargs)"""
    def __str__(self):
        return self.card_number

    #Declaration de la methode get_decrypted_number pour decrypter le champ card_number
    def get_number(self):
        # Déchiffrement du numéro lors de la récupération
        return decrypter(self.card_number)
