from django.contrib.auth import views
from django.urls import path

from . import app_views

app_name = 'fish_app'

urlpatterns = [
    path('', app_views.index, name='index'),
    path('login/', views.auth_login, name='login'),
    # path('registration/', views.registration, name='registration'),
    path('get_places/', app_views.get_places, name='get_places'),
    path('get_place_info/', app_views.get_place_info, name='get_place_info'),
    path('add_place/', app_views.add_place, name='add_place'),
    # path('<int:place_id>/', views.detail, name='detail'),
    # path('<int:place_id>/leave_comment', views.leave_comment, name='leave_comment')
]
