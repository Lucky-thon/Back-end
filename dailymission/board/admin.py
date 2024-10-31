# board/admin.py
from django.contrib import admin
from .models import MissionSuccessPost, RecruitmentPost

# 모델을 Django Admin에 등록
admin.site.register(MissionSuccessPost)
admin.site.register(RecruitmentPost)
