from django.contrib import admin
from .models import RecruitmentPost, RecruitmentComment

@admin.register(RecruitmentPost)
class RecruitmentPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # 관리자에서 보여줄 필드
    search_fields = ('title', 'content')  # 검색 기능 추가

@admin.register(RecruitmentComment)
class RecruitmentCommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'post', 'writer', 'create_at')  # 관리자에서 보여줄 필드
    search_fields = ('comment',)  # 검색 기능 추가