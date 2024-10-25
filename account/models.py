from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class User(models.Model):
    nom = models.CharField(max_length=100)
    mail = models.EmailField()
    password = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.nom


