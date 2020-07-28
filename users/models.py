from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models


class YamUser(AbstractUser):
    bio = models.TextField(blank=True)
