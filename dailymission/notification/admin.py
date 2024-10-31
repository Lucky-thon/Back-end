# notification/admin.py
from django.contrib import admin
from .models import Notification

# Notification 모델을 Django Admin에 등록
admin.site.register(Notification)
