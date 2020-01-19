from django.urls import path

from . import views

app_name = 'fish_app'

urlpatterns = [
    path('', views.index, name='fish_app'),
    # path('<int:place_id>/', views.detail, name='detail'),
    # path('<int:place_id>/leave_comment', views.leave_comment, name='leave_comment')
]