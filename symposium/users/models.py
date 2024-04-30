from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import UserManager
from django.utils import timezone
import string, random

class User(AbstractUser):
    email = models.EmailField(unique=True, null=True, db_index=True)
    username = models.CharField(max_length=20, default=None, unique=True)
    first_name = models.CharField(max_length=20, null=False, )
    last_name = models.CharField(max_length=20, null=False)
    phone_number = models.BigIntegerField(null=False, unique=True, blank=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.user.username)