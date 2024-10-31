# board/views.py
from django.shortcuts import render, redirect
from .forms import MissionSuccessPostForm
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import MissionSuccessPost
from .serializers import MissionSuccessPostSerializer

def mission_success_list(request):
    posts = MissionSuccessPost.objects.all()
    return render(request, 'board/mission_success_list.html', {'posts': posts})

@login_required # 로그인 된 사람만 사용 할 수 있도록 함.
def mission_success_create(request):
    if request.method == 'POST':
        form = MissionSuccessPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('mission_success_list')
    else:
        form = MissionSuccessPostForm()
    return render(request, 'board/mission_success_create.html', {'form': form})

class MissionSuccessPostListAPI(generics.ListAPIView):
    queryset = MissionSuccessPost.objects.all()
    serializer_class = MissionSuccessPostSerializer

class MissionSuccessPostCreateAPI(generics.CreateAPIView):
    queryset = MissionSuccessPost.objects.all()
    serializer_class = MissionSuccessPostSerializer
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 게시글 작성 가능