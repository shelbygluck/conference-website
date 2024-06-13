# Creating custom user model for Django
# The custom user needs to have fields for address, zip code, city and state
# The custom user also needs to have a field for the user's phone number

from django.db import models
from django.contrib.auth.models import AbstractUser

class ConferenceUser(AbstractUser):
    # Override first_name and last_name to make required
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
