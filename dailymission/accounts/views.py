from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def account_home(request):
    return render(request, 'accounts/home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '로그인 성공!')
            return redirect('home')  # 로그인 후 이동할 URL
        else:
            messages.error(request, '잘못된 사용자 이름 또는 비밀번호입니다.')

    return render(request, 'accounts/login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 자동으로 로그인
            messages.success(request, '회원가입 성공!')
            return redirect('account_home')  # 회원가입 후 이동할 URL
        else:
            # 오류 메시지를 출력합니다.
            for error in form.errors.values():
                messages.error(request, error)  # 모든 오류를 메시지로 추가
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})
