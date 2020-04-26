from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=128)
    photo = models.FileField()
    description = models.TextField()
    birthday = models.DateField()

class Channel(models.Model):
    channel_id = models.CharField(max_length=128, primary_key= True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    publishedAt = models.DateTimeField()
    thumbnail = models.URLField()
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    country = models.CharField(max_length=3)
    viewCount = models.PositiveIntegerField()
    videoCount = models.PositiveIntegerField()
    subscriberCount = models.PositiveIntegerField()
    playlist_id = models.CharField(max_length=128)

    def __str__(self):
        return self.title
    
class Profile_Channel(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel ,on_delete=models.CASCADE)

class Video(models.Model):
    video_id = models.CharField(max_length=128, primary_key = True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField()
    thumbnail = models.URLField()
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    
    
class Video_Statistic(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    publishedAt = models.DateField(auto_now=False, auto_now_add=False)
    viewAt = models.DateField()
    viewCount = models.PositiveIntegerField()
    likeCount = models.PositiveIntegerField()
    dislikeCount = models.PositiveIntegerField()
    commentCount = models.PositiveIntegerField()

    def __str__(self):
        return self.publishedAt