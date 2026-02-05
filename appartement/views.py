from django.shortcuts import render
from .models import Appartement

def accueil(request):
    appartements = Appartement.objects.filter(disponible=True)
    return render(request, 'accueil.html', {'appartement':appartements})
# Create your views here.

# Create your views here.
