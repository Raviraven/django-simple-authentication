from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, email):
        if not username and not password:
            raise ValueError("User must have username and password")

        user = self.model(
            username=username,
            email=email
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, email):

        user = self.create_superuser(
            username,
            password,
            email
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    is_admin = models.BooleanField(default=False)

    some_additional_property = models.CharField(max_length=200)

    objects = CustomUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.USERNAME_FIELD

    @property
    def is_admin(self):
        return self.is_admin

