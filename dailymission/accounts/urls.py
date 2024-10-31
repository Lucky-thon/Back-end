from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_home, name='account_home'),  # 기본 뷰를 정의
    path('login/', views.login_view, name='login'),  # 로그인 뷰
    path('register/', views.register_view, name='register'),  # 회원가입 뷰
    # 필요한 다른 URL 패턴 추가
]
