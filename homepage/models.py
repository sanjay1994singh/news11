from django.db import models


# Create your models here.
class Follow(models.Model):
    follow = models.BigIntegerField(null=True, blank=True)
