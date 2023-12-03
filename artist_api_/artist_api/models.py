# artist_api/models.py
from django.contrib.auth.models import User
from django.db import models

class Work(models.Model):
    LINK_TYPES = (
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('OT', 'Other'),
    )

    link = models.URLField()
    work_type = models.CharField(max_length=2, choices=LINK_TYPES)

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    works = models.ManyToManyField(Work)

def create_artist(sender, instance, created, **kwargs):
    if created:
        Artist.objects.create(user=instance, name=instance.username)

# Connect the signal
models.signals.post_save.connect(create_artist, sender=User)
