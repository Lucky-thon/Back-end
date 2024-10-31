# notification/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .tasks import create_notification
from board.models import MissionSuccessPost, RecruitmentPost
from comments.models import Comment

@receiver(post_save, sender=Comment)
def send_notification_on_comment(sender, instance, created, **kwargs):
    if created:
        print("Comment created. Signal triggered.")  # 디버깅 메시지 추가
        try:
            post = instance.post  # 댓글이 달린 게시글 객체
            post_author = post.author
            if post_author != instance.author:
                message = f"{instance.author.username}님이 회원님의 게시글에 댓글을 남겼습니다."
                content_type = ContentType.objects.get_for_model(post)
                create_notification.delay(
                    post_author.id, message, content_type.id, post.id
                )
            print("Notification task scheduled.")  # 디버깅 메시지 추가
        except Exception as e:
            print("Error in signal:", e)
