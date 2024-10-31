# comments/admin.py
from django.contrib import admin
from .models import Comment

# Comment 모델을 Django Admin에 등록
admin.site.register(Comment)
