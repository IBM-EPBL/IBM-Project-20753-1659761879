import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   

    def __str__(self):
        return f"{self.username}"

    # def get_obsolute_url(self):
    #     return reverse('dashboard', kwargs={
    #         'id': str(self.id)
    #     })
    

