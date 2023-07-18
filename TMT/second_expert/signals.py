from django.dispatch import receiver
from django.contrib import messages
from django.contrib.auth.signals import user_logged_in, user_logged_out
from .models import UserProfile

@receiver(user_logged_in)
def user_logged_in_handler(sender, user, request, **kwargs):
    profile = UserProfile.objects.get(user=user)
    messages.success(request, f"Welcome back, {profile.username}!")

@receiver(user_logged_out)
def user_logged_out_handler(sender, user, request, **kwargs):
    messages.success(request, "You have been logged out!")
