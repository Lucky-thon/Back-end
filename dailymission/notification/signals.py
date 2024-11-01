from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .tasks import create_notification
from board.models import RecruitmentComment

@receiver(post_save, sender=RecruitmentComment)
def send_notification_on_comment(sender, instance, created, **kwargs):
    if created:
        post = instance.post  # 댓글이 달린 게시글 객체
        post_author = post.author
        if post_author != instance.writer:  # 작성자와 댓글 작성자가 다를 때만 알림 생성
            message = f"{instance.writer.username}님이 회원님의 게시글에 댓글을 남겼습니다."
            content_type = ContentType.objects.get_for_model(post)
            create_notification.delay(
                post_author.id, message, content_type.id, post.id
            )
