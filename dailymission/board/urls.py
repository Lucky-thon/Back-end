# board/urls.py
from django.urls import path
from . import views
from .views import MissionSuccessPostListAPI

urlpatterns = [
    path('mission-success/', views.mission_success_list, name='mission_success_list'), # 미션 성공 게시판
    path('mission-success/create/', views.mission_success_create, name='mission_success_create'), # 미션 성공 게시판 작성
    path('api/mission-success/', MissionSuccessPostListAPI.as_view(), name='mission_success_list_api'), # 미션 성공 게시판 api
]
