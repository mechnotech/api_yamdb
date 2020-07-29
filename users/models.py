from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models


class YamUser(AbstractUser):
    ROLES = [
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    ]

    bio = models.TextField(blank=True)
    code = models.IntegerField()
    role = models.CharField(
        max_length=9,
        choices=ROLES,
        default='user',
    )
