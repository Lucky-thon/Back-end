from django.contrib import admin
from .models import RecruitmentPost, RecruitmentComment, MissionSuccessPost

@admin.register(RecruitmentPost)
class RecruitmentPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # 관리자에서 보여줄 필드
    search_fields = ('title', 'content')  # 검색 기능 추가

@admin.register(RecruitmentComment)
class RecruitmentCommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'post', 'writer', 'create_at')  # 관리자에서 보여줄 필드
    search_fields = ('comment',)  # 검색 기능 추가

# MissionSuccessPost 모델을 어드민에 등록
@admin.register(MissionSuccessPost)
class MissionSuccessPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # 어드민에서 보이는 필드 설정
    search_fields = ('title', 'content')  # 검색 기능 추가
    list_filter = ('created_at', 'author')  # 필터 추가