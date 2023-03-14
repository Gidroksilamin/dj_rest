from django.db import models
from django.contrib.auth.models import AbstractUser


class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    organizations = models.ManyToManyField(Organization)
