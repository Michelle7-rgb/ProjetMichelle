from django.shortcuts import render
from .models import Appartement, AppartementImage
from django.shortcuts import get_object_or_404, redirect

# gestion des vues pour l'application appartement

#accueil
def accueil(request):
    appartements = Appartement.objects.filter(disponible=True)
    return render(request, 'accueil.html', {'appartements':appartements})

# gestion des appartements
from django.core.exceptions import PermissionDenied

def ajouter_appartement(request):
    if not request.user.is_authenticated or request.user.role != 'PROPRIETAIRE':
        raise PermissionDenied

    if request.method == 'POST':
        appartement = Appartement.objects.create(
            titre=request.POST.get('titre'),
            type_logement=request.POST.get('type_logement'),
            quartier=request.POST.get('quartier'),
            prix=request.POST.get('prix'),
            description=request.POST.get('description'),
            proprietaire=request.user,
            contact_proprietaire=request.POST.get('contact'),
        )

        # images multiples
        for file in request.FILES.getlist('images'):
            AppartementImage.objects.create(
                appartement=appartement,
                image=file
            )

        return redirect('appartement_detail', pk=appartement.id)

    return render(request, 'ajouter_appartement.html')

def supprimer_appartement(request, id):
    appartement = get_object_or_404(Appartement, id=id)

    if request.user != appartement.proprietaire:
        raise PermissionDenied

    appartement.delete()
    return redirect('feed')
 

def modifier_appartement(request, id):
    appartement = get_object_or_404(Appartement, id=id)

    if request.user != appartement.proprietaire:
        raise PermissionDenied

    if request.method == 'POST':
        appartement.titre = request.POST.get('titre')
        appartement.prix = request.POST.get('prix')
        appartement.description = request.POST.get('description')
        appartement.save()

        return redirect('appartement_detail', pk=appartement.id)

    return render(request, 'modifier_appartement.html', {'appartement': appartement})


def appartement_detail(request, pk):
    appartement = get_object_or_404(Appartement, pk=pk)
    images = appartement.images.all()

    return render(request, 'appartement_detail.html', {
        'appartement': appartement,
        'images': images
    })

def liste_appartements(request):
    appartements = Appartement.objects.filter(disponible=True)

    quartier = request.GET.get('quartier')
    type_logement = request.GET.get('type')
    prix_max = request.GET.get('prix')

    if quartier:
        appartements = appartements.filter(quartier__icontains=quartier)

    if type_logement:
        appartements = appartements.filter(type_logement=type_logement)

    if prix_max:
        appartements = appartements.filter(prix__lte=prix_max)

    context = {
        'appartements': appartements
    }
    return render(request, 'feed.html', context)