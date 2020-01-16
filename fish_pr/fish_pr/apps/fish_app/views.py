from django.shortcuts import render
from .models import FishingPlace, Order
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

def index(request):
    places = FishingPlace.objects.order_by('-id')
    return render(request, 'fish_app/list.html', {'places': places})

def detail(request, place_id):
    try:
        p = FishingPlace.objects.get( id=place_id)
    except:
        raise Http404("Данные не найдены!.." )

    latest_order_list = p.order_set.order_by('-id')[:10]

    return render(request, 'fish_app/detail.html', {'place': p, 'latest_order_list': latest_order_list})

def leave_comment(request, place_id):
    try:
        p = FishingPlace.objects.get(id=place_id)
    except:
        raise Http404("Данные не найдены!..")

    p.order_set.create(user_id=2, description=request.POST['description'], photos="pic.jpg")
    return HttpResponseRedirect(reverse('fish_app:detail', args=(p.id,)))

