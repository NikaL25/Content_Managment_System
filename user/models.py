from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    description = models.TextField(blank=True)
    is_author = models.BooleanField(default=False)

    def __str__(self):
        return self.email