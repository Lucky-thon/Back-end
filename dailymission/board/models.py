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
    post = models.ForeignKey(RecruitmentPost, related_name='comments', on_delete=models.CASCADE)  # 댓글이 속한 게시글
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 댓글 작성자
    content = models.TextField()  # 댓글 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 댓글 작성일자