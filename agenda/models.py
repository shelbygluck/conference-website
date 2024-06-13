from django.db import models
from django.core.validators import RegexValidator
from conference_auth.models import ConferenceUser
from django.urls import reverse_lazy

# Create your models here.
# Creating a site for a conference
# Potential speakers will submit talks for approval
# Talks will be approved or rejected by staff

# Create status choices
STATUS_CHOICES = (
    ('submitted', 'Submitted'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
)

class Track(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Talk(models.Model):
    title = models.CharField(max_length=255, unique=True)
    abstract = models.TextField()
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='submitted')
    track = models.ForeignKey(Track, on_delete=models.PROTECT)
    speaker = models.ForeignKey(ConferenceUser, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('talks-detail', args=[str(self.id)])
