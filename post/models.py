from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    header_image = models.ImageField(upload_to='post_image', null=True, blank=True)
    inner_image = models.ImageField(upload_to='post_image', null=True, blank=True)
    views = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
