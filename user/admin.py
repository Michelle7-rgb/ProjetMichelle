from django.contrib import admin
from .models import Locataire
from .models import Proprietaire

admin.site.register(Locataire)
admin.site.register(Proprietaire)

# Register your models here.
