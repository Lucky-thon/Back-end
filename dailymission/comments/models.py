from django.db import models
from django.contrib.auth.models import User
from board.models import MissionSuccessPost, RecruitmentPost

class Comment(models.Model):
    post = models.ForeignKey(MissionSuccessPost, on_delete=models.CASCADE)  # 게시글 연결
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
