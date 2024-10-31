# notification/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.NotificationListAPI.as_view(), name='notification_list'),
]
