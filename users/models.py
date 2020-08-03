from django.contrib.auth.models import AbstractUser
from django.db import models


class YamUser(AbstractUser):
    ROLES = [
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    ]

    email = models.EmailField('email address', unique=True)
    bio = models.TextField(blank=True, null=True)
    code = models.CharField(blank=True, null=True, max_length=100)
    role = models.CharField(
        max_length=9,
        choices=ROLES,
        default='user',
    )
