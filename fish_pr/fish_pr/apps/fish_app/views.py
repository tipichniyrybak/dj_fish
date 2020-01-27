from django.shortcuts import render
from .models import FishingPlace, Order
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
from ftplib import FTP
from werkzeug.utils import secure_filename
import os
from django.core.files.storage import default_storage


def index(request):
    places = FishingPlace.objects.order_by('-id')
    return render(request, 'fish_app/index.html', {'places': places})

@csrf_exempt
def get_places(request):
    places = FishingPlace.objects.values()
    return JsonResponse(list(places), safe=False)

@csrf_exempt
def get_place_info(request):
    place_id = request.POST.get("place_id")
    place = FishingPlace.objects.filter(id=place_id).values()
    return JsonResponse(list(place), safe=False)

@csrf_exempt
def add_place(request):
    data = request.POST.get('place_name')
    files = request.files.getlist
    place = FishingPlace(name=data.get('place_name'), lant=data.get('place_lant'), long=data.get('place_long'), description=data.get('place_description'), photos=data.get('place_photos'))
    id = place.save()
    if id != 0:
        ftp = FTP()
        ftp.connect('ftpupload.net', 21)
        ftp.login('epiz_24989236', 'FIbPfZKy3F')
        FTP_path = "/htdocs/media/img/places/" + str(id)
        if not FTP_path in ftp.nlst():
            ftp.mkd(FTP_path)
        ftp.cwd(FTP_path)

        for photo in request.files.getlist('files[]'):
            file_name = default_storage.save(photo.name, photo)
            filename = secure_filename(photo.filename)
            file_path = os.path.join(static, 'img/tmp_places_photo' + filename)
            photo.save(file_path)
            fp = open(file_path, 'rb')
            ftp.storbinary('STOR %s' % os.path.basename(filename), fp, 1024)
            os.remove(file_path)
            fp.close()

    return JsonResponse(id, safe=False)


# def detail(request, place_id):
#     try:
#         p = FishingPlace.objects.get( id=place_id)
#     except:
#         raise Http404("Данные не найдены!.." )
#
#     latest_order_list = p.order_set.order_by('-id')[:10]
#
#     return render(request, 'workspace/detail.html', {'place': p, 'latest_order_list': latest_order_list})
#
# def leave_comment(request, place_id):
#     try:
#         p = FishingPlace.objects.get(id=place_id)
#     except:
#         raise Http404("Данные не найдены!..")
#
#     p.order_set.create(user_id=2, description=request.POST['description'], photos="pic.jpg")
#     return HttpResponseRedirect(reverse('workspace:detail', args=(p.id,)))
