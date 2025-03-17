from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Ensure email is unique
    twitter_access_token = models.CharField(max_length=255, blank=True, null=True)
    facebook_access_token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username  # ✅ String representation for better admin display
