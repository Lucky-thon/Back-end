# board/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MissionSuccessPost, UserProfile

@receiver(post_save, sender=MissionSuccessPost)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, _ = UserProfile.objects.get_or_create(user=instance.author)
        profile.has_posted_in_mission_success = True
        profile.save()
