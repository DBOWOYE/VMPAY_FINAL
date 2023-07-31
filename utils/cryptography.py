from cryptography.fernet import Fernet

with open("./my_key.txt", "rb") as my_key:
    key = my_key.read()
#Instanciation de Fernet
fernet = Fernet(key)

#Fonction de cryptage
def crypter(val):
    return fernet.encrypt(val.encode()).decode()

#Fonction de decryptage
def decrypter(val):
    return fernet.decrypt(val.encode()).decode()
