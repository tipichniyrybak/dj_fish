from django.shortcuts import render
from .models import FishingPlace, Order
from django.http import Http404, HttpResponseRedirect

def index(request):
    places = FishingPlace.objects.order_by('-id')
    return render(request, 'fish_app/list.html', {'places': places})

def detail(request, place_id):
    try:
        p = FishingPlace.objects.get( id=place_id)
    except:
        raise Http404("Данные не найдены!.." )
    return render(request, 'fish_app/detail.html', {'place': p})

def leave_comment(request, place_id):
    pass
