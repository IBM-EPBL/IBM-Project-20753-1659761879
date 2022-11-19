import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   

    def __str__(self):
        return f"{self.username}"



class Profile(models.Model):
    class Gender(models.TextChoices):
        male = "Male",
        female = "Female"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='profile_user', on_delete=models.CASCADE)
    specialization = models.CharField(max_length = 50, blank=False)
    interested_domains = models.CharField(max_length=300, blank=False)
    skills = models.CharField(max_length=200, blank=False)
    address1 = models.CharField(max_length=400, blank=False)
    address2 = models.CharField(max_length=400, blank=False)
    country = models.CharField(max_length=100)
    pincode = models.IntegerField(blank= False, null=True) #fix max value
    gender = models.CharField(max_length=20, choices=Gender.choices)



    
    def __str__(self):
        return f"{self.user}"

    

