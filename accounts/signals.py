from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser, CustomUserProfile


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    """
    Create a user profile for every new account created.
    """
    if created:
        CustomUserProfile.objects.create(user=instance)


def save_profile(sender, instance, **kwargs):
    """
    Save the user profile.
    """
    instance.profile.save()
