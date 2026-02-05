from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    isOwner = models.BooleanField(default=False)
    phoneNuber = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class Locataire(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    telephone = models.IntegerField(max_length=10)
    email = models.EmailField()
    mot_de_passe = models.IntegerField()
    photo_profil = models.CharField()
    date_creation = models.DateField() 

    def __str__(self):
        return self.email
    
class Proprietaire(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    telephone = models.IntegerField(max_length=10)
    email = models.EmailField()
    mot_de_passe = models.IntegerField()
    photo_profil = models.CharField()
    date_creation = models.DateField() 
    type_proprietaire = models.CharField(max_length=20)
    statut_compte = models.IntegerField()

    def __str__(self):
        return self.nom 
    

    
# Create your models here.
