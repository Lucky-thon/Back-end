# board/models.py
from django.db import models
from django.contrib.auth.models import User

class MissionSuccessPost(models.Model):
    title = models.CharField(max_length=100) # 제목
    content = models.TextField() # 내용
    image = models.ImageField(upload_to='mission_images/', blank=True, null=True) # 이미지
    created_at = models.DateTimeField(auto_now_add=True) # 작성일시
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 작성자

    def __str__(self):
        return self.title


class RecruitmentPost(models.Model):
    title = models.CharField(max_length=100)  # 제목
    content = models.TextField()               # 내용
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성자
    created_at = models.DateTimeField(auto_now_add=True)       # 작성일자

    def __str__(self):
        return self.title

class RecruitmentComment(models.Model):
    comment = models.TextField() # 댓글 내용
    create_at = models.DateTimeField(auto_now_add=True) # 댓글 생성일
    post = models.ForeignKey(RecruitmentPost, on_delete=models.CASCADE)  # 어떤 게시물에 달린 댓글인지 알 수 있는 게시글
    writer = models.ForeignKey(User, on_delete=models.CASCADE)  # 댓글 작성자

    def __str__(self):
        return self.comment

# 사용자 프로필 모델
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_posted_in_mission_success = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
