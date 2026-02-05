from django.db import models

class Appartement(models.Model):
     titre = models.CharField()
     type_logement = models.CharField()
     quartier = models.CharField()
     prix = models.IntegerField()
     description = models.TextField()
     photo = models.CharField()
     contact_proprietaire = models.CharField()
     disponible = models.CharField()
     date_publication = models.DateField()
     
# Create your models here.
