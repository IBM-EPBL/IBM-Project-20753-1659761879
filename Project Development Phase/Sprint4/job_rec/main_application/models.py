import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings
from accounts.models import Profile

class JobApplied(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Profile, related_name='job_profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=300, blank=True)
    location = models.CharField(max_length=500, blank=True)
    company_name = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.user}"

