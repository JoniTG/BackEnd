from django.db import models
from django.utils import timezone

class Photo(models.Model):
    url = models.CharField(max_length=1000)
    time_created = models.DateTimeField('Date created')

class User(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    time_created = models.DateTimeField('date created')
    last_active = models.DateTimeField('last active date')

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    content_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    content_text = models.CharField(max_length=1000)






