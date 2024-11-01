# notification/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.NotificationListAPI.as_view(), name='notification_list'),
    path('unread_check/', views.UnreadNotificationCheckAPI.as_view(), name='unread_notification_check'),
]
