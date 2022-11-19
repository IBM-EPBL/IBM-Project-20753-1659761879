from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import Profile

CustomUser = get_user_model()

@receiver(user_signed_up)
def user_signed_up_set_profile(request, user, **kwargs):
    current_user = CustomUser.objects.get(email=user.email)
    object = Profile(user=current_user)
    object.save()