from django.urls import path

from . import views

app_name = 'fish_app'

urlpatterns = [
    path('', views.index, name='fish_app'),
    path('get_places/', views.get_places, name='get_places'),
    path('get_place_info/', views.get_place_info, name='get_place_info'),
    # path('<int:place_id>/', views.detail, name='detail'),
    # path('<int:place_id>/leave_comment', views.leave_comment, name='leave_comment')
]
