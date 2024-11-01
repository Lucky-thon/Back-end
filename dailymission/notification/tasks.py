# notification/tasks.py
from celery import shared_task
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from .models import Notification

@shared_task
def create_notification(user_id, message, content_type_id, object_id):
    user = User.objects.get(id=user_id)
    content_type = ContentType.objects.get_for_id(content_type_id)

    if content_type.model == 'recruitmentpost':
        target_url = f"/recruitment/{object_id}/"
    else:
        target_url = None

    Notification.objects.create(
        user=user,
        message=message,
        content_type=content_type,
        object_id=object_id,
        target_url=target_url
    )
