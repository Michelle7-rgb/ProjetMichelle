from django.urls import path
from .views import accueil

urlpatterns = [
    path('log/', accueil, name='accueil'),
]

# Create your views here.
