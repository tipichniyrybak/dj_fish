from django.shortcuts import render
from .models import FishingPlace, Order
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers


def index(request):
    places = FishingPlace.objects.order_by('-id')
    return render(request, 'fish_app/index.html', {'places': places})

@csrf_exempt
def get_places(request):
    places = FishingPlace.objects.values('id', 'name', 'lant', 'long', 'description', 'photos')
    return JsonResponse(list(places), safe=False)

@csrf_exempt
def get_place_info(request):
    place_id = request.POST.get("place_id")
    print ('place_id = ', place_id)
    place = FishingPlace.objects.values('id', 'name', 'lant', 'long', 'description', 'photos').get(id=place_id)

    return JsonResponse(list(place), safe=False)



def detail(request, place_id):
    try:
        p = FishingPlace.objects.get( id=place_id)
    except:
        raise Http404("Данные не найдены!.." )

    latest_order_list = p.order_set.order_by('-id')[:10]

    return render(request, 'workspace/detail.html', {'place': p, 'latest_order_list': latest_order_list})

def leave_comment(request, place_id):
    try:
        p = FishingPlace.objects.get(id=place_id)
    except:
        raise Http404("Данные не найдены!..")

    p.order_set.create(user_id=2, description=request.POST['description'], photos="pic.jpg")
    return HttpResponseRedirect(reverse('workspace:detail', args=(p.id,)))
