from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    is_admin = models.BooleanField(default=False)

    some_additional_property = models.CharField(max_length=200)

    # objects = MyUserManager()
    USERNAME_FIELD = username
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return self.USERNAME_FIELD

    @property
    def is_admin(self):
        return self.is_admin
