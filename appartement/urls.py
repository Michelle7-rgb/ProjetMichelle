from django.urls import path
from .views import accueil, ajouter_appartement, feed, supprimer_appartement, modifier_appartement, appartement_detail

urlpatterns = [
    #path('log/', accueil, name='accueil'),
    path('', accueil, name='accueil'),
    path("feed/", feed, name="feed"),
    path("ajouter/", ajouter_appartement, name="ajouter_appartement"),
    path("appartement/<int:pk>/", appartement_detail, name="appartement_detail"),
    path("appartement/<int:id>/modifier/", modifier_appartement, name="modifier_appartement"),
    path("appartement/<int:id>/supprimer/", supprimer_appartement, name="supprimer_appartement"),

   # path('profile/', profile, name='profile'),
    
]

# Create your views here.
