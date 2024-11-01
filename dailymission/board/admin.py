from django.contrib import admin
from .models import RecruitmentPost, RecruitmentComment, MissionSuccessPost, UserProfile

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

# UserProfile 모델 등록
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'has_posted_in_mission_success')  # 확인할 필드 추가
    search_fields = ('user__username',)  # 사용자 이름으로 검색 가능
    list_filter = ('has_posted_in_mission_success',)  # 필터 옵션 추가