from django.db import models


# Create your models here.

class LiveVideo(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    video_link = models.TextField()
    views = models.IntegerField()
    likes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
