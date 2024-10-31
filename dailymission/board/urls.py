# board/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('mission-success/', views.mission_success_list, name='mission_success_list'),
    path('mission-success/create/', views.mission_success_create, name='mission_success_create'),
]
