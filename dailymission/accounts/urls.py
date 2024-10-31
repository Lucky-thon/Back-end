from django.urls import path
from . import views
from .views import LoginAPIView, ProtectedView

urlpatterns = [
    path('', views.account_home, name='account_home'),  # 기본 뷰를 정의
    path('login/', views.login_view, name='login'),  # 로그인 뷰
    path('register/', views.register_view, name='register'),  # 회원가입 뷰
    path('api/login/', LoginAPIView.as_view(), name='api_login'), # 로그인 api
    path('api/protected/', ProtectedView.as_view(), name='protected_view'), #
]
