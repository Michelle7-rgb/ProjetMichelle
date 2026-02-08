from django.urls import path
from .views import accueil

urlpatterns = [
    #path('log/', accueil, name='accueil'),
    path('', accueil, name='accueil'),

   # path('profile/', profile, name='profile'),
    
]

# Create your views here.
