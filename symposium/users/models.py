from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager
from django.utils import timezone

class User(AbstractUser):
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(unique=True, null=True)
    phone_number = models.BigIntegerField(null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    admin = models.BooleanField(default=False, null=False)

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.first_name

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin = models.BooleanField(default=False, null=False)

    def __str__(self):
        return str(self.user.email)