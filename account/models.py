from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


# Create your models here.


class User(AbstractUser):
    name = models.CharField("Name of User", blank=True, max_length=255)
    email = models.EmailField("email address", unique=True)
    username = None
    USERNAME_FIELD = "email"
    adresse = models.CharField(max_length=100)

    REQUIRED_FIELDS = []
    objects = UserManager()
    def __str__(self):
        return self.nom


