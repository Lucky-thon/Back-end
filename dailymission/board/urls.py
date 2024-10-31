# board/urls.py
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import MissionSuccessPostListAPI, MissionSuccessPostCreateAPI, RecruitmentPostListAPI, RecruitmentPostCreateAPI, RecruitmentCommentCreateAPI

router = DefaultRouter()
router.register(r'mission_success_posts', MissionSuccessPostListAPI, basename='mission-success-posts')

urlpatterns = [
    path('mission-success/', views.mission_success_list, name='mission_success_list'), # 미션 성공 게시판
    path('mission-success/create/', views.mission_success_create, name='mission_success_create'), # 미션 성공 게시판 작성
    path('api/mission-success/', MissionSuccessPostListAPI.as_view(), name='mission_success_list_api'), # 미션 성공 게시판 api
    path('api/mission-success/create/', MissionSuccessPostCreateAPI.as_view(), name='mission_success_post_create'),  # 게시글 작성 API
    path('api/recruitment/', RecruitmentPostListAPI.as_view(), name='recruitment_post_list'),  # 인원 모집 게시판
    path('api/recruitment/create/', RecruitmentPostCreateAPI.as_view(), name='recruitment_post_create'),  # 인원 모집 게시글 작성
    path('api/Recruitmentcomments/create/', RecruitmentCommentCreateAPI.as_view(), name='Recruitmentcomment-create'),
]
