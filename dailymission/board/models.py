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
