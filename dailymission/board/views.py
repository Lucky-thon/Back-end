# board/views.py
from django.shortcuts import render, redirect
from .forms import MissionSuccessPostForm
from django.contrib.auth.decorators import login_required
from .models import MissionSuccessPost
from .serializers import MissionSuccessPostSerializer
from .serializers import RecruitmentPostSerializer
from rest_framework.response import Response
import logging
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import RecruitmentComment, RecruitmentPost
from .serializers import RecruitmentCommentSerializer
from rest_framework import status

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

# 미션 성공 게시판 api
class MissionSuccessPostListAPI(generics.ListAPIView):
    queryset = MissionSuccessPost.objects.all()
    serializer_class = MissionSuccessPostSerializer

# 미션 성공 게시판 작성 api
class MissionSuccessPostCreateAPI(generics.CreateAPIView):
    queryset = MissionSuccessPost.objects.all()
    serializer_class = MissionSuccessPostSerializer
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 게시글 작성 가능

    def perform_create(self, serializer):
        logger.info(f"Author before save: {self.request.user}")  # 현재 사용자 로그
        serializer.save(author=self.request.user)  # 작성자로 현재 사용자 설정

    def post(self, request, *args, **kwargs):
        logger.info(f"Request data: {request.data}")
        logger.info(f"User: {request.user}")  # 사용자가 인증되었는지 확인
        return super().post(request, *args, **kwargs)


logger = logging.getLogger(__name__)

# 인원 모집 게시판 api
class RecruitmentPostListAPI(generics.ListAPIView):
    queryset = RecruitmentPost.objects.all()
    serializer_class = RecruitmentPostSerializer

# 인원 모집 게시판 작성 api
class RecruitmentPostCreateAPI(generics.CreateAPIView):
    queryset = RecruitmentPost.objects.all()
    serializer_class = RecruitmentPostSerializer
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 게시글 작성 가능

    def perform_create(self, serializer):
        logger.info(f"Author before save: {self.request.user}")  # 현재 사용자 로그
        serializer.save(author=self.request.user)  # 작성자로 현재 사용자 설정

    def post(self, request, *args, **kwargs):
        logger.info(f"Request data: {request.data}")
        logger.info(f"User: {request.user}")  # 사용자가 인증되었는지 확인
        return super().post(request, *args, **kwargs)

# 인원 모집 게시판 댓글 생성 api
class RecruitmentCommentCreateAPI(generics.CreateAPIView):
    serializer_class = RecruitmentCommentSerializer  # 추가: 사용될 직렬 변환기 설정
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 댓글 작성 가능

    def post(self, request, bid, *args, **kwargs):
        try:
            post = RecruitmentPost.objects.get(id=bid)
        except RecruitmentPost.DoesNotExist:
            return Response({"error": "게시글이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)  # 수정: get_serializer 메서드 사용
        if serializer.is_valid():
            serializer.save(post=post, writer=request.user)  # writer 값을 request.user로 설정
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


