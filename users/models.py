from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """ Replaces 'User' model provided by Django """

    # null - DB stores NULL as value
    # blank - form(s) allow an empty value for data entry
    age = models.PositiveIntegerField(null=True, blank=True)

### end ###
